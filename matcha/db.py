import psycopg2
from flask import g
from matcha import app

def connect_db():
    """Connects to the specific database."""
    rv = psycopg2.connect(**app.config['DATABASE'])
    rv.autocommit = True
    return rv


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'db'):
        g.db = connect_db()
    return g.db


def query_db(query, args=(), one=False):
    cursor = get_db().cursor()
    cur = cursor.execute(query, args)
    rv = cur.fetchall() if cur else None
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'db'):
        g.db.close()


def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
