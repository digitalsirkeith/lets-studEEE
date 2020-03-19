import os
from . import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY=config.SECRET_KEY, 
    SQLALCHEMY_DATABASE_URI=config.DATABASE_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .blueprints import home, verify
app.register_blueprint(home.bp)
app.register_blueprint(verify.bp)

CORS(app)