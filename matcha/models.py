import random, uuid, hashlib

from matcha import db, mail

def hash_password(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt



class User(object):

    def __init__(self, id=None, pseudo=None, email=None):
        if id: self.user = self.get_by_id(id)
        elif pseudo: self.user = self.get_by_username(pseudo)
        elif email: self.user = self.get_by_email(email)
        else: self.user = None

    def new(self, datas):
        datas['password'] = hash_password(datas['password'])
        query = """INSERT INTO Users (mail, username, password, first_name, last_name) VALUES (%s, %s, %s, %s, %s)"""
        res = db.query_db(query, args=(datas["email"], datas["username"], datas["password"], datas["firstname"], datas["lastname"]), fetch=False)
        self.user = self.get_by_username(datas["username"])
        return self.user

    def get_by_id(self, id):
        query = "SELECT * FROM Users WHERE users.id=%s"
        return db.query_db(query, args=(id,), one=True)

    def get_by_username(self, username):
        query = "SELECT * FROM Users WHERE users.username=%s"
        return db.query_db(query, args=(username,), one=True)

    def get_by_email(self, email):
        query = "SELECT * FROM Users WHERE users.mail=%s"
        return db.query_db(query, args=(email,), one=True)

    def user_exists(self, mail, username):
        query = "SELECT * FROM Users WHERE users.mail=%s OR users.username=%s"
        res = db.query_db(query, args=(mail, username), one=True)
        # query = "SELECT * FROM Users;"
        # res = db.query_db(query)
        if not res: return False
        if res["mail"]: return "A user with this email already exists"
        return "A user with this username already exists"

    def reset_password(self):
        new_password = ''.join(random.choice('0123456789ABCDEF') for i in range(5))
        query = "UPDATE Users SET password = %s WHERE id = %s"
        res = db.query_db(query, (hash_password(new_password), self.user['id']), fetch=False)
        mail.send_password_reset(self.user['mail'], new_password)