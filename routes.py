from app import app
from flask import render_template, request, session, redirect
import events, users

@app.route("/")
def index():
    list = events.get_events()
    return render_template("index.html", events=list)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        pwd = request.form["pwd"]
        if users.login(username, pwd):
            return redirect("/")
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
            return redirect("/")
        else:
            return render_template("error.html", message="Ongelma rekisteröinnissä.")

@app.route("/event", methods=["GET", "POST"])
def event():
    if request.method == "GET":
        return render_template("event.html")
    if request.method == "POST":
        name = request.form["name"]
        date = request.form["date"]
        description = request.form["description"]
        type = int(request.form["type"])
        open = int(request.form["open"])
        user_id = session["user_id"]
        if events.add_event(name, date, description, type, open, user_id):
            return redirect("/")
        else:
            return render_template("error.html", message="Ongelma tapahtuman lisäämisessä")

@app.route("/eventinfo/<int:id>", methods=["GET", "POST"])
def eventinfo(id):  
    list = events.event_info(id)
    return render_template("eventinfo.html", info=list)

   