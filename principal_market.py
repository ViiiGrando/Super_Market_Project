from flask import Flask, render_template,request,redirect
app = Flask(__name__)



@app.route("/")
def index():
 return render_template('index.html')




@app.route("/cart")
def cart():
    return render_template("/cart.html")

    


app.run(debug = True)