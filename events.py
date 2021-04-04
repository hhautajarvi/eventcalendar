from db import db

def get_events():
    sql = "SELECT E.name, E.date, E.id, E.description, E.type, E.open, U.name " \
        "FROM events E, users U WHERE U.id = E.user_id ORDER BY E.date"
    result = db.session.execute(sql)
    return result.fetchall()

def event_info(event_id):
    sql = "SELECT E.name, E.date, E.description, E.type, E.open, U.name " \
        "FROM events E, users U WHERE E.id=:event_id"
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