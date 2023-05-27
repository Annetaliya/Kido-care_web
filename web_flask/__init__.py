'''from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '9dc2caabe707156fda66b0ceeabda3ff'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    #from forms import LoginForm, RegistrationForm
    
    app.register_blueprint(views, url_prefix='/')
    
    from .models import User, Child, Report, Hospital, Doctor
    User = User()
    Child = Child()

    create_database()
    with app.app_context():
       db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'forms.LoginForm'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

def create_database():
    if not path.exists('kido-care_web/' + DB_NAME):
        db.create_all()
        print("Created Database!")
'''