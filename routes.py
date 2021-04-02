from app import app
from flask import render_template, request, session
import events, users

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/main", methods=["POST"])
def main():
    list = events.get_events()
    return render_template("main.html", name=session["name"], events=list)

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    pwd = request.form["pwd"]
    if users.login(username, pwd):
        return main()
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
            return main()
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
            return main()
        else:
            return render_template("error.html", message="Ongelma tapahtuman lisäämisessä")

   