from flask import Flask
from flask import render_template, redirect

app = app = Flask(__name__)


@app.route("/")
def homePage():
    return render_template("homePage.html")

@app.route("/pixiv")
def pixiv():
    return redirect("https://github.com/yusei27017/Pixiv")

@app.route("/aboutMe")
def aboutMe():
    return render_template("aboutMe.html")

@app.route("/aboutSite")
def aboutSite():
    return render_template("aboutSite.html")
