# import os
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_cors import CORS

# app = Flask(__name__, instance_relative_config=True)
# app.config.from_mapping(
#     SECRET_KEY=os.environ['SECRET_KEY'], 
#     SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL'],
#     SQLALCHEMY_TRACK_MODIFICATIONS=False
# )

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# from .database import init_app
# init_app(app)

# from .blueprints import root, create, add, quickcreate, show, display, tags, upload, random
# app.register_blueprint(root.bp)
# app.register_blueprint(create.bp)
# app.register_blueprint(add.bp)
# app.register_blueprint(show.bp)
# app.register_blueprint(display.bp)
# app.register_blueprint(quickcreate.bp)
# app.register_blueprint(tags.bp)
# app.register_blueprint(upload.bp)
# app.register_blueprint(random.bp)

# from .blueprints.json import show, create
# app.register_blueprint(show.bp)
# app.register_blueprint(create.bp)

# from flaskr.database import init_db
# init_db()

# try:
#     os.mkdir(os.getenv('FILES_LOC'))
# except FileExistsError:
#     pass
# try:
#     os.mkdir(os.getenv('TEMP_NAV_LOC'))
# except FileExistsError:
#     pass

# CORS(app)