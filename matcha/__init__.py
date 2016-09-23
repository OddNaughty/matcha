import os
from flask import Flask, url_for, render_template, request
app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'matcha.db'),
    SECRET_KEY='+qd=_k!t!t1qr*c7%v-x_m_)%py^3ulb=@9-9sjo7je%3nwevy',
    USERNAME='admin',
    PASSWORD='admin'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

import matcha.views
