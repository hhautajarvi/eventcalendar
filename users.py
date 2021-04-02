from db import db

def login(name, password):
    sql = "SELECT password FROM users WHERE name=:username"
    result = db.session.execute(sql, {"username":name})
    user = result.fetchone()  
    if user == None:
        return False
    else:
        if user[0] == password:
            return True

def register(name,password):
    try:
        sql = "INSERT INTO users (name, password) VALUES (:name, :password)"
        db.session.execute(sql, {"name":name, "password":password})
        db.session.commit()
    except:
        return False
    return login(name, password)
    