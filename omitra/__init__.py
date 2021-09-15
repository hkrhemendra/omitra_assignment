from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "THISISASCRET"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/omitra'
db = SQLAlchemy(app)

BASE_PATH = os.path.abspath(os.environ.get('HOME'))
print(BASE_PATH)
ALLOWED_EXTENSION = {'jpg','jpeg','mp4','mp3'}
