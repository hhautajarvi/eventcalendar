from db import db
from flask import session

def login(name, password):
    sql = "SELECT password, id FROM users WHERE name=:username"
    result = db.session.execute(sql, {"username":name})
    user = result.fetchone()  
    if user == None:
        return False
    else:
        if user[0] == password:
            session["user_id"] = user[1]
            session["name"] = name
            return True
        else:
            return False

def register(name,password):
    try:
        sql = "INSERT INTO users (name, password) VALUES (:name, :password)"
        db.session.execute(sql, {"name":name, "password":password})
        db.session.commit()
    except:
        return False
    return login(name, password)

def logout():
    del session["user_id"]
    del session["name"]