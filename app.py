from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from os import getenv


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.secret_key = getenv("SECRET_KEY")
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/main", methods=["POST"])
def main(name):
    list = get_events()
    return render_template("main.html", name=name, events= list)

def get_events():
    sql = "SELECT E.name, E.date, E.description, E.type, E.open, U.name FROM events E, users U WHERE U.id = E.user_id ORDER BY E.date"
    result = db.session.execute(sql)
    return result.fetchall()


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    pwd = request.form["pwd"]
    sql = "SELECT password FROM users WHERE name=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()    
    if user == None:
        return render_template("error.html", message="Väärä tunnus")
    else:
        if user[0] == pwd:
            return main(username)
        else:
            return render_template("error.html", message="Väärä salasana")

@app.route("/register", methods= ["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        sql = "INSERT INTO users (name, password) VALUES (:name, :password)"
        db.session.execute(sql, {"name":name, "password":password})
        db.session.commit()
        return main(name)