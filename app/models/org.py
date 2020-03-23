from app import db

class Organization(db.Model):
    __tablename__ = 'organizations'


# class User(UserMixin, db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.Text, nullable=False, unique=True)
#     email = db.Column(db.String(255), nullable=False, unique=True)
#     password_hash = db.Column(db.String(255))
#     contact_number = db.Column(db.String(255), nullable=False)
#     roles = db.relationship('Role', secondary='user_roles')

#     def __init__(self, username, email, password, contact_number):
#         self.username = username
#         self.email = email
#         self.contact_number = contact_number
#         self.set_password(password)
#         self.roles = []

#     def set_password(self, password):
#         self.password_hash = security.generate_password_hash(password)

#     def check_password(self, password):
#         return security.check_password_hash(self.password_hash, password)

# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), unique=True)

#     def __init__(self, name):
#         self.name = name

# class UserRole(db.Model):
#     __tablename__ = 'user_roles'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey(User.id, ondelete='CASCADE'))
#     role_id = db.Column(db.Integer, db.ForeignKey(Role.id, ondelete='CASCADE'))