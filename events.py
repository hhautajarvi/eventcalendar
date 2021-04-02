from db import db

def get_events():
    sql = "SELECT E.name, E.date, E.description, E.type, E.open, U.name " \
        "FROM events E, users U WHERE U.id = E.user_id ORDER BY E.date"
    result = db.session.execute(sql)
    return result.fetchall()
    