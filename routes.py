from app import app
from flask import render_template, request, session, redirect
import events, users, participants
from datetime import date

@app.route("/")
def index():
    if session:
        list = events.get_events(0)
        user_id=session["user_id"]
    else:
        list = []
        user_id = 0
    return render_template("index.html", events=list, user_id=user_id, selected=0)

@app.route("/event_type", methods=["POST"])
def event_type():
    if session:
        type = int(request.form["type"])
        list = events.get_events(type)
        user_id=session["user_id"]
        return render_template("index.html", events=list, user_id=user_id, selected=type)
    else:
        return render_template("error.html", message="Et ole kirjautunut sisään")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html", error=False, message="")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["pwd"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("login.html", error=True, message="Väärä salasana tai tunnus")

@app.route("/register", methods= ["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html", error=False, message="")
    if request.method == "POST":
        name = request.form["name"]
        if len(name) < 1 or len(name) > 30:
            return render_template("register.html", error=True, message="Anna nimi 1-30 merkin pituisena")
        password = request.form["password"]
        password_check = request.form["password_check"]
        if password == "":
            return render_template("register.html", error=True, message="Anna myös salasana")
        if password == password_check:
            if users.username_register_check(name) == None:
                if users.register(name, password):
                    return redirect("/")
                else:
                    return render_template("error.html", message="Ongelma rekisteröinnissä.")
            else:
                return render_template("register.html", error=True, message="Käyttäjänimi on jo olemassa")   
        else:
            return render_template("register.html", error=True, message="Salasanat eivät täsmää")

@app.route("/logout")
def logout():
    if session:
        users.logout()
        return redirect("/")
    else:
        return render_template("error.html", message="Et ole kirjautunut sisään")

@app.route("/event", methods=["GET", "POST"])
def event():
    if session:
        userlist = users.get_userlist()
        now = date.today()
        datenow = now.isoformat()
        if request.method == "GET":
            return render_template("event.html", userlist=userlist, today=datenow, message=None)
        if request.method == "POST":
            users.csrf_check(request.form["csrf_token"])
            name = request.form["name"]
            if name == "":
                return render_template("event.html", userlist=userlist, today=datenow, message="Anna tapahtumalle nimi")
            if len(name) > 30 or len(name) < 1:            
                return render_template("event.html", userlist=userlist, today=datenow, message="Anna nimi 1-30 merkin pituisena")
            eventdate = request.form["date"]
            if eventdate == "":
                return render_template("event.html", userlist=userlist, today=datenow, message="Anna päivämäärä")            
            location = request.form["location"]
            if len(location) > 100 or len(location) < 1:
                return render_template("event.html", userlist=userlist, today=datenow, message="Anna paikka 1-100 merkin pituisena")
            description = request.form["description"]
            if len(description) > 200:
                return render_template("event.html", userlist=userlist, today=datenow, message="Anna enintään 200 merkin kuvaus")
            type = int(request.form["type"])
            open = int(request.form["open"])
            user_id = session["user_id"]
            participant_list = request.form.getlist("invites")
            event_id = events.add_event(name, eventdate, description, type, open, user_id, location)
            if event_id != -1:
                if participants.add_participants(participant_list, event_id):
                    return redirect("/")
                else:
                    return render_template("error.html", message="Ongelma kutsujen lähettämisessä")
            else:
                return render_template("error.html", message="Ongelma tapahtuman lisäämisessä")
    else:
        return render_template("error.html", message="Et ole kirjautunut sisään")

@app.route("/eventinfo/<int:id>", methods=["GET"])
def eventinfo(id):  
    if session:
        list = events.event_info(id)
        userlist = participants.get_participants(id)
        event_owner = False
        if list[5] == session["name"]:
            event_owner = True
            allusers = users.get_userlist()
            invitees = participants.get_invitees(id)
            not_yet_invited = [user for user in allusers if user not in invitees]
        else:
            invitees = []
            not_yet_invited = []
        past = date.today() > list[1]
        return render_template("eventinfo.html", info=list, users=userlist[0], user_is_participant = userlist[1], 
        past=past, event_owner=event_owner, not_yet_invited=not_yet_invited, invitees=invitees)
    else:
        return render_template("error.html", message="Et ole kirjautunut sisään")

@app.route("/eventjoin/<int:id>", methods=["POST"])
def eventjoin(id):
    if session:
        users.csrf_check(request.form["csrf_token"])
        if request.form["join"] == "Yes":
            if participants.join_event(id):
                return redirect("/eventinfo/"+str(id))
            else:
                return render_template("error.html", message="Ongelma liittymisessä")
        else:
            return redirect("/eventinfo/"+str(id))
    else:
        return render_template("error.html", message="Et ole kirjautunut sisään")

@app.route("/eventexit/<int:id>", methods=["POST"])
def eventexit(id):
    if session:
        users.csrf_check(request.form["csrf_token"])
        if request.form["exit"] == "No":
            if participants.exit_event(id):
                return redirect("/eventinfo/"+str(id))
            else:
                return render_template("error.html", message="Ongelma poistumisessa")
        else:
            return redirect("/eventinfo/"+str(id))
    else:
        return render_template("error.html", message="Et ole kirjautunut sisään")

@app.route("/eventdelete/<int:id>", methods=["POST"])
def eventdelete(id):
    if session:
        users.csrf_check(request.form["csrf_token"])
        if events.delete_event(id):
            return redirect("/")
        else:
            return render_template("error.html", message="Ongelma tapahtuman poistamisessa")
    else:
        return render_template("error.html", message="Et ole kirjautunut sisään")

@app.route("/pastevents", methods=["GET"])
def pastevents():
    if session:
        list = events.get_past_events()
        return render_template("pastevents.html", events=list)
    else:
        return render_template("error.html", message="Et ole kirjautunut sisään")

@app.route("/inviteusers/<int:id>", methods=["POST"])
def inviteusers(id):
    if session:
        users.csrf_check(request.form["csrf_token"])
        invite_list = request.form.getlist("invites")
        if participants.add_participants(invite_list, id):
            return redirect("/eventinfo/"+str(id))
        else:
            return render_template("error.html", message="Ongelma kutsujen lähettämisessä")
    else:
        return render_template("error.html", message="Et ole kirjautunut sisään")

@app.route("/editevent/<int:id>", methods=["GET", "POST"])
def editevent(id):
    if session:
        list = events.event_info(id)
        now = date.today()
        datenow = now.isoformat()
        if request.method == "GET":        
            if list[5] == session["name"]:
                return render_template("editevent.html", info=list, today=datenow, message=None)
            else:
                return render_template("error.html", message="Et ole tapahtuman luoja")
        if request.method == "POST":
            users.csrf_check(request.form["csrf_token"])
            name = request.form["name"]
            if name == "":
                return render_template("editevent.html", info=list, today=datenow, message="Anna tapahtumalle nimi")
            if len(name) > 30 or len(name) < 1:            
                return render_template("editevent.html", info=list, today=datenow, message="Anna nimi 1-30 merkin pituisena")
            eventdate = request.form["date"]
            if eventdate == "":
                return render_template("editevent.html", info=list, today=datenow, message="Anna päivämäärä")            
            location = request.form["location"]
            if len(location) > 100 or len(location) < 1:
                return render_template("editevent.html", info=list, today=datenow, message="Anna paikka 1-100 merkin pituisena")
            description = request.form["description"]
            if len(description) > 200:
                return render_template("editevent.html", info=list, today=datenow, message="Anna enintään 200 merkin kuvaus")
            type = int(request.form["type"])
            open = int(request.form["open"])
            if events.event_update(id, name, eventdate, description, type, open, location):
                return redirect("/eventinfo/"+str(id))
            else:
                return render_template("error.html", message="Ongelma tietojen päivittämisessä")
    else:
        return render_template("error.html", message="Et ole kirjautunut sisään")