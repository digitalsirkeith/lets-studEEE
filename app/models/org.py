import enum
from app import db
from app.models.user import User

class OrganizationRank(enum.Enum):
    owner = 1
    admin = 2
    active_member = 3
    inactive_member = 4

class OrganizationStatus(enum.Enum):
    pending = 1
    approved = 2
    denied = 3

class Organization(db.Model):
    __tablename__ = 'organizations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    members = db.relationship('OrganizationUser', back_populates='organization')
    posts = db.relationship('Post', back_populates='author_org')
    photo_url = db.Column(db.Text)
    verified = db.Column(db.Boolean, default=False)
    status = db.Column(db.Enum(OrganizationStatus))

    def __init__(self, name, email, owner, photo_url, status=OrganizationStatus.pending):
        self.name = name
        self.email = email
        if owner:
            self.members.append(OrganizationRank.create_owner(owner))
        self.photo_url = photo_url
        self.verified = False
        self.status = status

    @staticmethod
    def none():
        return Organization.query.get(1)

class OrganizationUser(db.Model):
    __tablename__ = 'organization_user'
    user_id = db.Column(db.Integer, db.ForeignKey(User.id, ondelete='CASCADE'), primary_key=True)
    organization_id = db.Column(db.Integer, db.ForeignKey(Organization.id, ondelete='CASCADE'), primary_key=True)
    rank = db.Column(db.Enum(OrganizationRank))

    user = db.relationship(User, back_populates='organizations')
    organization = db.relationship(Organization, back_populates='members')

    @staticmethod
    def create_owner(owner):
        association = OrganizationRank(rank=OrganizationRank.owner)
        association.user = owner
        return association
