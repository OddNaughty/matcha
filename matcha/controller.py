from flask import session, flash, g
import re, hashlib

from matcha import models


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


def do_register(datas):
    res = {'error': {}, 'datas': datas}
    errors = res['error']
    datas = dict(datas)
    for field in ["username", "firstname", "lastname", "email", "password"]:
        if not datas[field]:
            errors[field] = "A value is required"
    if errors: return res
    for k, v in datas.items():
        datas[k] = v[0].strip()
    if not re.match(r'[^@]+@[^@]+\.[^@]+', datas["email"]):
        errors["Email"] = "This is not a valid email"
    if len(datas["password"]) < 5:
        errors["Password"] = "The password must be at least 5 characters long"
    if errors: return res
    user = models.User().user_exists(datas["email"], datas["username"])
    if user: errors["User exists"] = user; return res
    user = models.User().new(datas)
    flash("You were successfully registered !")
    return res

def do_login(datas):
    res = {'error': {}, 'datas': datas}
    errors = res['error']
    datas = dict(datas)
    for field in ["email", "password"]:
        if not datas[field]:
            errors[field] = "A value is required"
    if errors: return res
    for k, v in datas.items():
        datas[k] = v[0].strip()
    if not re.match(r'[^@]+@[^@]+\.[^@]+', datas["email"]):
        errors["Email"] = "This is not a valid email"
    if len(datas["password"]) < 5:
        errors["Password"] = "The password must be at least 5 characters long"
    if errors: return res
    user = models.User(email=datas['email'])
    if not user or not user.user: errors["Email"] = "User with this email don't exists"; return res
    if check_password(user.user['password'], datas['password']) is False: errors["Password"] = "The password don't match"; return res
    session['user'] = dict(user.user)
    # print(session['user'])
    # g.logged_user = user
    # print(g.logged_user)
    flash("You are successfully logged in !")
    return res

def do_lost_password(datas):
    res = {'error': {}, 'datas': datas}
    errors = res['error']
    datas = dict(datas)
    for field in ["email"]:
        if not datas[field]:
            errors[field] = "A value is required"
    if errors: return res
    for k, v in datas.items():
        datas[k] = v[0].strip()
    if not re.match(r'[^@]+@[^@]+\.[^@]+', datas["email"]):
        errors["Email"] = "This is not a valid email"
    if errors: return res
    user = models.User(email=datas['email'])
    if not user or not user.user: errors["Email"] = "User with this email don't exists"; return res
    user.reset_password()
    flash("A mail containing the reseted password has been send !")
    return res

def do_logout():
    session.pop('user')
    # print(g.logged_user)
    # g.pop('logged_user')