from flask import Flask

from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.sql import func



app = Flask(__name__)
app.config['SECRET_KEY'] = '9dc2caabe707156fda66b0ceeabda3ff'
DB_NAME = "database.db"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db = SQLAlchemy(app)

from web_flask import routes