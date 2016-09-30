from flask import Flask, session, g
app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE= {"database": 'matcha', "user": 'cwagner'},
    SECRET_KEY='+qd=_k!t!t1qr*c7%v-x_m_)%py^3ulb=@9-9sjo7je%3nwevy',
    USERNAME='admin',
    PASSWORD='admin',
    SMTP_LOGIN = 'matcha.staff@gmail.com',
    SMTP_PASSWORD = 'supertoto'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

import matcha.views, matcha.models

@app.before_request
def before_request():
    if session.get('user', None) is not None:
        g.user = matcha.models.User(session['user']['id'])