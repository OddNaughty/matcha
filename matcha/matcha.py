from flask import render_template, url_for

from matcha import app


@app.route('/')
def index():
    login_url = url_for('login')
    return render_template("index.html", login_url=login_url)
