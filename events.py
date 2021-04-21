from db import db
from flask import session
from datetime import date

def get_events(type):
    datenow = date.today()
    if type == 0:
        sql = "SELECT E.name, E.date, E.id FROM events E, users U, invites I " \
            "WHERE E.visible = 1 AND U.id = E.user_id AND E.date>=:datenow AND (E.open = 1 OR (I.event_id = E.id AND I.user_id=:user) " \
            "OR E.user_id=:user) GROUP BY E.date, E.name, E.id ORDER BY E.date"
        result = db.session.execute(sql, {"user":session["user_id"], "datenow":datenow})
    else:
        sql = "SELECT E.name, E.date, E.id FROM events E, users U, invites I " \
            "WHERE E.visible = 1 AND U.id = E.user_id AND E.date>=:datenow AND E.type=:type AND " \
            "(E.open = 1 OR (I.event_id = E.id AND I.user_id=:user) OR E.user_id=:user) GROUP BY E.date, E.name, E.id ORDER BY E.date"
        result = db.session.execute(sql, {"user":session["user_id"], "datenow":datenow, "type":type})
    return result.fetchall()

def get_past_events():
    datenow = date.today()
    sql = "SELECT E.name, E.date, E.id FROM events E, users U, participants P " \
        "WHERE E.visible = 1 AND U.id = E.user_id AND E.date<:datenow AND (E.open = 1 OR (P.event_id = E.id AND P.user_id=:user) " \
        "OR E.user_id=:user) GROUP BY E.date, E.name, E.id ORDER BY E.date"
    result = db.session.execute(sql, {"user":session["user_id"], "datenow":datenow})
    return result.fetchall()

def event_info(event_id):
    sql = "SELECT E.name, E.date, E.description, E.type, E.open, U.name, E.id " \
        "FROM events E, users U WHERE E.id=:event_id AND E.user_id = U.id"
    result = db.session.execute(sql, {"event_id":event_id})
    return result.fetchone()

def add_event(name, date, description, type, open, user_id):
    try:
        visible = 1
        sql = "INSERT INTO events (name, date, description, type, open, user_id, visible) " \
            "VALUES (:name, :date, :description, :type, :open, :user_id, :visible) RETURNING id"
        idsearch = db.session.execute(sql, {"name":name, "date":date, "description":description, "type":type, "open":open, "user_id":user_id, "visible":visible})
        event_id = idsearch.fetchone()[0]
        sql2 = "INSERT INTO participants (event_id, user_id) VALUES (:event_id, :user_id)"
        db.session.execute(sql2, {"event_id":event_id, "user_id":user_id})
        db.session.commit()
        return event_id
    except:
        return -1

def delete_event(id):
    try:
        sql = "UPDATE events SET visible=0 WHERE id=:id"
        db.session.execute(sql, {"id":id})
        db.session.commit()
        return True
    except:
        return False