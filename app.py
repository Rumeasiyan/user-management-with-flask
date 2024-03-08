from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/user-account/")
def userAccount():
    return render_template("/user/index.html")


@app.route("/service-account/")
def serviceAccound():
    return render_template("/provider/index.html")


@app.route("/reset-password/")
def reset():
    return render_template("/reset/index.html")


@app.route("/change-password/")
def changePassword():
    return render_template("/reset/change-password.html")
