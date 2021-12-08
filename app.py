from flask import Flask, jsonify
from flask import render_template, redirect
# from flask import request, send_from_directory
from flask_pymongo import PyMongo

app = app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/flaskBlog"
mongo = PyMongo(app)

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

@app.route("/pixivPage")
def pixivPage():
    return render_template("pixivPage.html")

@app.route("/ps5Page")
def ps5Page():
    return render_template("ps5Page.html")

@app.route("/skillPage")
def skillPage():
    return render_template("skillPage.html")

@app.route("/aboutJp")
def aboutJp():
    return render_template("aboutJp.html")

@app.route("/linkPage")
def linkPage():
    return render_template("linkPage.html")

@app.route("/aboutMeData")
def aboutMeData():
    res = mongo.db.aboutMe.find({'sort':'aboutMe'})
    for v in res:
        data = v['data']
    return jsonify(data=data)

@app.route("/projectData")
def projectData():
    res = mongo.db.aboutMe.find({'sort':'projectInfo'})
    for v in res:
        data = v['data']
    return jsonify(data=data)

@app.route("/footerData")
def footerData():
    res = mongo.db.aboutMe.find({'sort':'footer'})
    for v in res:
        data = v['data']
    return jsonify(data=data)

@app.route("/linkData")
def linkData():
    res = mongo.db.aboutMe.find({'sort':'linkData'})
    for v in res:
        data = v['data']
    return jsonify(data=data)

# @app.route("/sitemap.xml")
# def sitemap():
#     return render_template("sitemap.xml")


