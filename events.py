from db import db
from flask import session

def get_events():
    sql = "SELECT E.name, E.date, E.id FROM events E, users U, participants P " \
        "WHERE U.id = E.user_id AND (E.open = 1 OR (P.event_id = E.id AND P.user_id=:user) " \
        "OR E.user_id=:user) GROUP BY E.date, E.name, E.id"
    result = db.session.execute(sql, {"user":session["user_id"]})
    return result.fetchall()

def event_info(event_id):
    sql = "SELECT E.name, E.date, E.description, E.type, E.open, U.name, E.id " \
        "FROM events E, users U WHERE E.id=:event_id AND E.user_id = U.id"
    result = db.session.execute(sql, {"event_id":event_id})
    return result.fetchone()

def add_event(name, date, description, type, open, user_id):
    try:
        sql = "INSERT INTO events (name, date, description, type, open, user_id) " \
            "VALUES (:name, :date, :description, :type, :open, :user_id) RETURNING id"
        idsearch = db.session.execute(sql, {"name":name, "date":date, "description":description, "type":type, "open":open, "user_id":user_id})
        event_id = idsearch.fetchone()[0]
        sql2 = "INSERT INTO participants (event_id, user_id) VALUES (:event_id, :user_id)"
        db.session.execute(sql2, {"event_id":event_id, "user_id":user_id})
        db.session.commit()
        return True
    except:
        return False