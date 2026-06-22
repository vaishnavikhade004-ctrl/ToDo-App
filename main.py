from flask import Flask 
from flask import render_template 
app=Flask(__name__,template_folder="templates")
@app.route("/")
def home():
    return render_template("Home.html")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
@app.route("/register")
def register():
    return render_template("register.html")
@app.route("/login")
def login():
    return render_template("login.html")
if __name__=="__main__":
    app.run()

