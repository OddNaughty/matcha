from flask import url_for, render_template, request
from matcha import app, controller

@app.route('/')
def index():
    login_url = url_for('login')
    return render_template("index.html", login_url=login_url)

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        error = controller.do_register(request.form)
    return render_template("register.html", error=error)
