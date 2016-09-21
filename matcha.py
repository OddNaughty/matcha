# all the imports
import os

from flask import Flask


# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'matcha.db'),
    SECRET_KEY='+qd=_k!t!t1qr*c7%v-x_m_)%py^3ulb=@9-9sjo7je%3nwevy',
    USERNAME='admin',
    PASSWORD='admin'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)



from db import init_db

@app.cli.command('initdb')
def k():
    init_db()
    print('Database initialized')