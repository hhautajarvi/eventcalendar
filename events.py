from db import db

def get_events():
    sql = "SELECT E.name, E.date, E.description, E.type, E.open, U.name " \
        "FROM events E, users U WHERE U.id = E.user_id ORDER BY E.date"
    result = db.session.execute(sql)
    return result.fetchall()

def add_event(name, date, description, type, open, user_id):
    try:
        sql = "INSERT INTO events (name, date, description, type, open, user_id) " \
            "VALUES (:name, :date, :description, :type, :open, :user_id)"
        db.session.execute(sql, {"name":name, "date":date, "description":description, "type":type, "open":open, "user_id":user_id})
        db.session.commit()
        return True
    except:
        return False