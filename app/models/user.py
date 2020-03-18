from .. import db
import enum

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    roles = db.relationship('Role', secondary='user_role')

    def __init__(self, username, email, roles):
        self.username = username
        self.email = email
        self.roles = roles

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __init__(self, name):
        self.name = name

class UserRole(db.Model):
    __tablename__ = 'user_roless'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id, ondelete='CASCADE'))
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id, ondelete='CASCADE'))