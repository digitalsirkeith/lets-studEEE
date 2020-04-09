from dotenv import load_dotenv
load_dotenv()
import os
from app.config import DevelopmentConfig, ProductionConfig
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_login import LoginManager
from dropbox import Dropbox

db = SQLAlchemy()
dropbox = Dropbox(os.getenv('DBX_ACCESS_TOKEN'))

def create_app(config_class=ProductionConfig):
    app = Flask(__name__)

    if os.getenv('FLASK_ENV') == 'development':
        app.config.from_object(DevelopmentConfig)
    else:
        app.config.from_object(config_class)

    with app.app_context():
        db.init_app(app)
        migrate = Migrate(app, db)
        login_manager = LoginManager(app)
        CORS(app)

        from app.blueprints import root, verify, auth, org, changepw
        app.register_blueprint(root.bp)
        app.register_blueprint(verify.bp)
        app.register_blueprint(auth.bp)
        app.register_blueprint(org.bp)
        app.register_blueprint(changepw.bp)

        from app.database import init_app
        init_app(app)

        from app.models.user import User, Role, UserRole
        from app.models.org import Organization, OrganizationUser
        from app.models.forum import Post, Comment
        from app.models.study import Topic, StudySession, StudySessionRating, StudySessionTopic, StudySessionMember

        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))

        return app