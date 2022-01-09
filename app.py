from flask import Flask, render_template,request
import mysql.connector

app=Flask(__name__)



@app.route('/')
def login():
 return render_template('login.html')

@app.route('/register')
def about():
     return render_template('register.html')

@app.route('/home')
def home():
     return render_template('home.html')

@app.route('/validation', methods=["GET","POST"])
def validation():
    email=request.form.get('email')
    password=request.form.get('password')
    return "The email is {} and the password is {}".format(email,password)

if __name__=="__main__":
     app.run(debug=True)
     