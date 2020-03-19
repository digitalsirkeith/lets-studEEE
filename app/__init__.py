import os
from . import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_login import LoginManager

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY=config.SECRET_KEY, 
    SQLALCHEMY_DATABASE_URI=config.DATABASE_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)

from .blueprints import root, verify
app.register_blueprint(root.bp)
app.register_blueprint(verify.bp)

from app.database import init_app
init_app(app)

CORS(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)