from app import app
from flask import render_template, request, session, redirect
import events, users, participants

@app.route("/")
def index():
    if session:
        list = events.get_events()
    else:
        list = []
    return render_template("index.html", events=list)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["pwd"]
        if users.login(username, password):
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

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

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

@app.route("/eventinfo/<int:id>", methods=["GET"])
def eventinfo(id):  
    list = events.event_info(id)
    userlist = participants.get_participants(id)
    return render_template("eventinfo.html", info=list, users=userlist[0], user_is_participant = userlist[1])

@app.route("/eventjoin<int:id>", methods=["POST"])
def eventjoin(id):
    if request.form["yes"] == "1":
        if participants.join_event(id):
            return redirect("/")
        else:
            return render_template("error.html", message="Ongelma liittymisessä")
    else:
        return redirect("/")

@app.route("/eventexit<int:id>", methods=["POST"])
def eventexit(id):
    if request.form["yes"] == "1":
        if participants.exit_event(id):
            return redirect("/")
        else:
            return render_template("error.html", message="Ongelma poistumisessa")
    else:
        return redirect("/")