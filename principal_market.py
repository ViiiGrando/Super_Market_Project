from flask import Flask, render_template,request,redirect, session
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)


@app.route("/")
def index():
   if 'user' in session:
        return redirect('/')
   else:
        return render_template('login.html')
 


@app.route("/login")
def login(): 
        return render_template('login.html')


@app.route("/register")
def register():
    return redirect('register.html')

@app.route("/cart")
def cart():
    return render_template('/cart.html')

    


app.run(debug = True)