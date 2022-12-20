from flask import Flask
from flask_sqlalchemy import SQLALchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
app.config['SECRET_KEY'] = '65a19a98-e2d1-4bfa-98bf-a8feec4ec0ed'

db = SQLAlchemy(app)
ma = Marshmallow(app)

from app import models