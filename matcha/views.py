from flask import url_for, render_template, request, redirect, g
from matcha import app, controller, utils

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/logout')
def logout():
    controller.do_logout()
    return redirect(url_for('index'))

@app.route('/login', methods=["GET", "POST"])
def login():
    res = {}
    if request.method == "POST":
        res = controller.do_login(request.form)
        print(res)
        if not res.get('error'): return redirect(url_for('index'))
    return render_template("login.html", error=res.get('error'), datas=res.get('datas'))


@app.route('/register', methods=["GET", "POST"])
def register():
    res = {}
    if request.method == "POST":
        res = controller.do_register(request.form)
        if not res.get('error'): return redirect(url_for('login'))
    return render_template("register.html", error=res.get('error'), datas=res.get('datas'))

@app.route('/lost_password', methods=["GET", "POST"])
def login_lost_password():
    res = {}
    if request.method == "POST":
        res = controller.do_lost_password(request.form)
        if not res.get('error'): return redirect(url_for('login'))
    return render_template("login_lost_password.html", error=res.get('error'), datas=res.get('datas'))

@app.route('/settings', methods=["GET", "POST"])
@utils.login_required
def settings():
    res = {}
    if request.method == "POST":
        res = controller.do_register(request.form)
        if not res.get('error'): return redirect(url_for('index'))
    res['datas'] = dict(g.user.user)
    return render_template("settings.html", error=res.get('error'), datas=res.get('datas'))
