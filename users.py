from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(name, password):
    sql = "SELECT password, id FROM users WHERE name=:username"
    result = db.session.execute(sql, {"username":name})
    user = result.fetchone()  
    if user == None:
        return False
    else:
        if check_password_hash(user[0], password):
            session["user_id"] = user[1]
            session["name"] = name
            return True
        else:
            return False

def register(name,password):
    try:
        hash_value = generate_password_hash(password)
        sql = "INSERT INTO users (name, password) VALUES (:name, :password)"
        db.session.execute(sql, {"name":name, "password":hash_value})
        db.session.commit()
    except:
        return False
    return login(name, password)

def logout():
    del session["user_id"]
    del session["name"]

def get_userlist():
    sql = "SELECT name, id FROM users WHERE id<>:user_id"
    result = db.session.execute(sql, {"user_id":session["user_id"]})
    return result.fetchall()