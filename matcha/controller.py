import re

from matcha import db


def do_register(datas):
    errors = {}
    for field in ["username", "firstname", "lastname", "email", "password"]:
        if not datas[field]:
            errors[field] = "A value is required"
    if errors: return errors
    if not re.match(r'[^@]+@[^@]+\.[^@]+', datas["email"]):
        errors["Email"] = "This is not a valid email"
    if len(datas["password"]) < 5:
        errors["Password"] = "The password must be at least 5 characters long"
    if errors: return errors
    query = ("INSERT INTO Users (mail, username, password, first_name, last_name)\n"
             "            VALUES (%s, %s, %s, %s, %s)")
    # cursor = db.get_db()
    # cursor.execute(query, (datas["email"], datas["username"], datas["password"], datas["firstname"], datas["lastname"]))
    # print(cursor)
    res = db.query_db(query, args=(datas["email"], datas["username"], datas["password"], datas["firstname"], datas["lastname"]))
    print(res)