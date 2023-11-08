import sqlite3


def get_db():
    try:
        db = sqlite3.connect('data.db')
        db.row_factory = sqlite3.Row
        return db
    except Exception as e:
        return str(e)


def execute_query(query, values=None):
    db = get_db()
    cursor = db.cursor()
    try:
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        db.commit()
        db.close()
        return True
    except Exception as e:
        db.rollback()
        db.close()
        return str(e)
