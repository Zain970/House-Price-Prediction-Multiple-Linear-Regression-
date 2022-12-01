from flask import Flask, render_template, url_for, request
import mysql.connector
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


app = Flask(__name__, static_folder='static')


# Connection to the database
myDb = mysql.connector.connect(host="localhost",
                             user="root",
                             password="zain12345",
                             database="myData")

if myDb :
    print("Connection Successful")

# Obtaining cursor object#
Cur=myDb.cursor()

# Main route for taking input for the values of the house
Cur=myDb.cursor()
@app.route("/")
def index():
        query="select * from Data"
        Cur.execute(query)
        data = Cur.fetchall()

        for d in data:
                print(d[1])
        print("Total number of rows in table: ", Cur.rowcount)
        return render_template('home.html',data=data)

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
            bedroom = int(request.form['bedrooms'])
            bathroom = int(request.form['bathrooms'])
            area = float(request.form['area'])
            property_type= (request.form['property_type'])
            location = (request.form['location'])
            city = (request.form['city'])

            change2=pd.read_csv("hello.csv")

            X = change2.drop(['price'], axis='columns')
            y = change2.price
            model = LinearRegression()
            model.fit(X, y)


            x = np.zeros(360)
            x[0] = bathroom
            x[1] = bedroom
            x[2] = area

            house_price=model.predict([x])[0]

            return render_template('house_price.html', stage=int(house_price))

if __name__ == "__main__":

    app.run(debug=True)
