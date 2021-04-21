from app import app
from flask import render_template, request, session, redirect
import events, users, participants
from datetime import date

@app.route("/")
def index():
    if session:
        list = events.get_events()
        #user_id=session["user_id"]
    else:
        list = []
        #user_id = 0
    return render_template("index.html", events=list)#, user_id=user_id)

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
        if len(name) < 1 or len(name) > 30:
            return render_template("error.html", message="Anna nimi 1-30 merkin pituisena")
        password = request.form["password"]
        password_check = request.form["password_check"]
        if password == "":
            return render_template("error.html", message="Anna myös salasana")
        if password == password_check:
            if users.username_register_check(name) == None:
                if users.register(name, password):
                    return redirect("/")
                else:
                    return render_template("error.html", message="Ongelma rekisteröinnissä.")
            else:
                return render_template("error.html", message="Käyttäjänimi on jo olemassa")   
        else:
            return render_template("error.html", message="Salasanat eivät täsmää")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/event", methods=["GET", "POST"])
def event():
    if request.method == "GET":
        userlist = users.get_userlist()
        now = date.today()
        datenow = now.isoformat()
        return render_template("event.html", userlist=userlist, today=datenow)
    if request.method == "POST":
        name = request.form["name"]
        if name == "":
            return render_template("error.html", message="Anna tapahtumalle nimi")
        if len(name) > 30 or len(name) < 1:
            return render_template("error.html", message="Anna nimi 1-30 merkin pituisena")
        eventdate = request.form["date"]
        description = request.form["description"]
        if len(description) > 200:
            return render_template("error.html", message="Anna enintään 200 merkin kuvaus")
        type = int(request.form["type"])
        open = int(request.form["open"])
        user_id = session["user_id"]
        participant_list = request.form.getlist("invites")
        event_id = events.add_event(name, eventdate, description, type, open, user_id)
        if event_id != -1:
            participants.add_participants(participant_list, event_id)
            return redirect("/")
        else:
            return render_template("error.html", message="Ongelma tapahtuman lisäämisessä")

@app.route("/eventinfo/<int:id>", methods=["GET"])
def eventinfo(id):  
    list = events.event_info(id)
    event_owner = False
    if list[5] == session["name"]:
        event_owner = True
    userlist = participants.get_participants(id)
    past = date.today() > list[1]
    return render_template("eventinfo.html", info=list, users=userlist[0], user_is_participant = userlist[1], past=past, event_owner=event_owner)

@app.route("/eventjoin<int:id>", methods=["POST"])
def eventjoin(id):
    if request.form["join"] == "Yes":
        if participants.join_event(id):
            return redirect("/")
        else:
            return render_template("error.html", message="Ongelma liittymisessä")
    else:
        return redirect("/")

@app.route("/eventexit<int:id>", methods=["POST"])
def eventexit(id):
    if request.form["exit"] == "No":
        if participants.exit_event(id):
            return redirect("/")
        else:
            return render_template("error.html", message="Ongelma poistumisessa")
    else:
        return redirect("/")

@app.route("/eventdelete<int:id>", methods=["POST"])
def eventdelete(id):
    if request.form["delete"] == "Yes":
        if events.delete_event(id):
            return redirect("/")
        else:
            return render_template("error.html", message="Ongelma tapahtuman poistamisessa")
    else:
        return redirect("/")

@app.route("/pastevents", methods=["GET"])
def pastevents():
    list = events.get_past_events()
    return render_template("pastevents.html", events=list)