from flask import Flask

from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.sql import func
from flask_bcrypt import Bcrypt
from flask_login import LoginManager






app = Flask(__name__)
app.config['SECRET_KEY'] = '9dc2caabe707156fda66b0ceeabda3ff'
DB_NAME = "database.db"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from web_flask import routes
from web_flask import db

db.create_all()