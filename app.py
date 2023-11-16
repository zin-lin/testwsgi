from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from uuid import *
import os

app = Flask(__name__)
db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inst.db'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

db.init_app(app)
# Create database
with app.app_context():
    db.create_all()
    db.session.commit()

# get unique id
def get_uid():
    return uuid4().hex

@app.route('/')
def hello_world():  # put application's code here
    nower = get_uid()
    base = os.path.join('instance', f'{nower}.txt')
    with open(base, 'w') as file:
        file.write('hell')
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
