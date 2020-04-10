import enum
from app import db
from app.models.user import User

class OrganizationRank(enum.Enum):
    owner = 1
    admin = 2
    active_member = 3
    inactive_member = 4
    applicant = 5

class OrganizationStatus(enum.Enum):
    pending = 1
    approved = 2
    denied = 3
    unverified = 4

class OrganizationUser(db.Model):
    __tablename__ = 'organization_user'
    user_id = db.Column(db.Integer, db.ForeignKey(User.id, ondelete='CASCADE'), primary_key=True)
    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id', ondelete='CASCADE'), primary_key=True)
    _rank = db.Column(db.Integer)

    user = db.relationship(User, back_populates='organizations')
    organization = db.relationship('Organization', back_populates='members')

    @staticmethod
    def create_owner(owner):
        with db.session.no_autoflush:
            association = OrganizationUser(_rank=OrganizationRank.owner.value)
            association.user = owner
        return association

    @property
    def rank(self):
        return OrganizationRank(self._rank) if self._rank else None

class Organization(db.Model):
    __tablename__ = 'organizations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    members = db.relationship(OrganizationUser, back_populates='organization')
    posts = db.relationship('Post', back_populates='author_org')
    photo_url = db.Column(db.Text)
    _status = db.Column(db.Integer)
    description = db.Column(db.Text)

    def __init__(self, name, email, owner, description, status=OrganizationStatus.unverified):
        self.name = name
        self.email = email
        if owner:
            self.members.append(OrganizationUser.create_owner(owner))
        self._status = status.value
        self.description = description

    @staticmethod
    def none():
        return Organization.query.get(1)

    @property
    def status(self):
        return OrganizationStatus(self._status)if self._status else None

    def cloud_dir(self):
        return f'/org/{self.id:06d}.png'

    def add_applicant(self, user):
        with db.session.no_autoflush:
            association = OrganizationUser(_rank=OrganizationRank.applicant.value)
            association.user = user
            self.members.append(association)