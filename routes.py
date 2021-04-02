from app import app
from flask import render_template, request
import events, users

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/main", methods=["POST"])
def main(name):
    list = events.get_events()
    return render_template("main.html", name=name, events=list)

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    pwd = request.form["pwd"]
    if users.login(username, pwd):
        return main(username)
    else:
        return render_template("error.html", message="Väärä salasana tai tunnus")

@app.route("/register", methods= ["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        if users.register(name, password):
            return main(name)
        else:
            return render_template("error.html", message="Ongelma rekistöröinnissä.")
   