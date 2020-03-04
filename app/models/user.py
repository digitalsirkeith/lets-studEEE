from .. import db
import enum

class AccountType(enum.Enum):
    Student = 1
    Admin = 2

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    account_type = db.Column(db.Enum(AccountType))

    def __init__(self, username, account_type):
        self.username = username
        self.account_type = account_type
        