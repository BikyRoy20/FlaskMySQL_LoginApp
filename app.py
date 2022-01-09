from flask import Flask, render_template,request
import mysql.connector

app=Flask(__name__)


conn=mysql.connector.connect(host="remotemysql.com",user="anupam",password="royanupam",database="flasklogin")
cursor=conn.cursor()


@app.route('/')
def login():
 return render_template('login.html')



@app.route('/register')
def about():
     return render_template('register.html')



@app.route('/home')
def home():
     return render_template('home.html')



# For LOGIN  ( when the user is already registred in the website)

@app.route('/validation', methods=["GET","POST"])
def validation():
    email=request.form.get('email')
    password=request.form.get('password')
    
    cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE  '{}' AND `password` LIKE '{}'""" ).format(email,password)
    users=cursor.fetchcall()

    if len(users)>0:
         return render_template('login.html')
    else:
         return render_template('login.html')    




# For REGISTRATION of NEW ACCOUNT FOR NEW USER

@app.route('/add_user',methods=['POST'])
def add_user():
     name=request.form.get('uname')
     email=request.form.get('uemail')
     password=request.form.get('upassword')
     cursor.execute("""INSERT INTO `users` (`user_id`,`name`,`email`,`password`)VALUES (NULL, '{}','{}','{}')""".format(name,email,password))
     conn.commit()

     return "USER REGISTERED SUCCESSFULLY"



if __name__=="__main__":
     app.run(debug=True)
     