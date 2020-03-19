from .. import db
import enum

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    contact_number = db.Column(db.String(255), nullable=False)
    roles = db.relationship('Role', secondary='user_roles')

    def __init__(self, username, email, password, contact_number):
        self.username = username
        self.email = email
        self.contact_number = contact_number
        self.password = password
        self.roles = []

    @staticmethod
    def get(self, user_id):
        return self.query.filter(self.id == user_id).one_or_none()

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __init__(self, name):
        self.name = name

class UserRole(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id, ondelete='CASCADE'))
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id, ondelete='CASCADE'))