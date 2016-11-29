import random, uuid, hashlib

from matcha import db, mail


def hash_password(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


class Gender(object):
    def __init__(self, gender_name=None):
        self.name = gender_name
        self.id = None
        self.name, self.id = self.get_object()

    def get_object(self):
        query = "SELECT * FROM genders WHERE gender=%s OR genders.id = %s"
        res = db.query_db(query, args=(self.name, self.id), one=True)
        if not res:
            return self.name, self.id
        return res.name, res.id

    # def add_gender(self, gender_name):
    #     query = "INSERT INTO genders (gender) VALUES (%s)"
    #     res = db.query_db(query, args=(gender_name,))
    #     self.gender = self.get_gender(gender_name)
    #     return self.gender

    def save(self):
        if self.id:
            query = "UPDATE Genders SET gender = %s WHERE id = %s"
            args = (self.gender, self.id)
        else:
            query = "INSERT INTO genders (gender) VALUES (%s)"
            args = (self.gender,)
        db.query_db(query, args, fetch=False)
        self.id, self.gender = self.get_object()
        return self

class User(object):
    def __init__(self, id=None, username=None, email=None):
        if id:
            user = self.get_by_id(id)
        elif username:
            user = self.get_by_username(username)
        elif email:
            user = self.get_by_email(email)
        else:
            user = None
        if user:
            self.id = user['id']
            self.mail = user['mail']
            self.username = user['username']
            self.first_name = user['first_name']
            self.last_name = user['last_name']
            self.creation_time = user['creation_time']
            self.gender_id = user['gender_id']
            self.password = user['password']
        else:
            self.id = None

    def new(self, datas):
        datas['password'] = hash_password(datas['password'])
        query = """INSERT INTO Users (mail, username, password, first_name, last_name) VALUES (%s, %s, %s, %s, %s)"""
        res = db.query_db(query, args=(
        datas["email"], datas["username"], datas["password"], datas["firstname"], datas["lastname"]), fetch=False)
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
        if not res: return False
        if res["mail"] == mail: return "A user with this email already exists"
        return "A user with this username already exists"

    def reset_password(self):
        new_password = ''.join(random.choice('0123456789ABCDEF') for i in range(5))
        query = "UPDATE Users SET password = %s WHERE id = %s"
        res = db.query_db(query, (hash_password(new_password), self.user['id']), fetch=False)
        mail.send_password_reset(self.user['mail'], new_password)

    def add_gender(self, gender_name):
        gender = Gender(gender_name)
        if not gender.id:
            gender.save()
        query = "UPDATE Users SET gender_id = %s WHERE id = %s"
        res = db.query_db(query, (gender.id, self.id), fetch=False)
        self.gender = gender