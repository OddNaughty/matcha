# all the imports

from flask import render_template, url_for

from matcha import app


@app.route('/')
def index():
    login_url = url_for('login')
    return render_template("index.html", login_url=login_url)


#
# from db import init_db
#
# @app.cli.command('initdb')
# def k():
#     init_db()
#     print('Database initialized')