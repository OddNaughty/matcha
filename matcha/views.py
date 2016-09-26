from flask import url_for, render_template, request, flash
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
        error = controller.do_register()
        # error = {"email":"This is not a valid email"}
    # flash("The method you used is get")
    # flash("The method you used is kaka")
    return render_template("register.html", error=error)
