from db import db
from flask import session

def get_participants(event_id):
    user_is_participant = False
    sql = "SELECT U.name FROM users U, participants P WHERE P.event_id=:event_id AND P.user_id = U.id"
    result = db.session.execute(sql, {"event_id":event_id})
    list = result.fetchall()
    for user in list:
        if user[0] == session["name"]:
            user_is_participant = True
    return list, user_is_participant

def join_event(event_id):
    try:
        sql = "INSERT INTO participants (event_id, user_id) VALUES (:event_id, :user_id)"
        db.session.execute(sql, {"event_id":event_id, "user_id":session["user_id"]})
        db.session.commit()    
        return True
    except:
        return False

def add_participants(participant_list, event_id):
    for participant in participant_list:
        sql = "INSERT INTO participants (event_id, user_id) VALUES (:event_id, :user_id)"
        db.session.execute(sql, {"event_id":event_id, "user_id":participant})
    db.session.commit()
    return

def exit_event(event_id):
    try:
        sql = "DELETE FROM participants WHERE event_id=:event_id AND user_id=:user_id"
        db.session.execute(sql, {"event_id":event_id, "user_id":session["user_id"]})
        db.session.commit()
        return True
    except:
        return False
