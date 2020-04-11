from werkzeug import security
from flask_login import UserMixin
from app import db

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __init__(self, name):
        self.name = name

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(255))
    contact_number = db.Column(db.String(255), nullable=False)
    photo_url = db.Column(db.Text)
    verified = db.Column(db.Boolean, default=False)

    posts = db.relationship('Post', back_populates='author_user')
    roles = db.relationship('Role', secondary='user_roles')
    organizations = db.relationship('OrganizationUser', back_populates='user')

    def __init__(self, username, email, password, contact_number):
        self.username = username
        self.email = email
        self.contact_number = contact_number
        self.set_password(password)
        self.roles = []
        self.photo_url = None
        self.verified = False

    def set_password(self, password):
        self.password_hash = security.generate_password_hash(password)

    def check_password(self, password):
        return security.check_password_hash(self.password_hash, password)

    def cloud_dir(self):
        return f'/user/{self.id:06d}.png'

    @property
    def is_admin(self):
        return Role.query.filter(Role.name == 'admin').one() in self.roles

class UserRole(db.Model):
    __tablename__ = 'user_roles'
    user_id = db.Column(db.Integer, db.ForeignKey(User.id, ondelete='CASCADE'), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id, ondelete='CASCADE'), primary_key=True)