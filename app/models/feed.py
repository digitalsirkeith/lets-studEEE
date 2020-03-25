from app import db
from app.models.user import User
from app.models.org import Organization

class Post(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    author_user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    author_org_id = db.Column(db.Integer, db.ForeignKey(Organization.id))
    date_posted = db.Column(db.Date)

    author_user = db.relationship(User, back_populates='posts')
    author_org = db.relationship(Organization, back_populates='posts')
    comments = db.relationship('Comment')

    def __init__(self, title, content, date_posted, author_user, author_org):
        self.title = title
        self.content = content
        self.author_user = author_user
        self.date_posted = date_posted
        if author_org:
            self.author_org = author_org
        else:
            self.author_org = Organization.none()
        self.comments = []

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    author_user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    author_org_id = db.Column(db.Integer, db.ForeignKey(Organization.id))
    post_id = db.Column(db.Integer, db.ForeignKey(Post.id))
    content = db.Column(db.Text)
    date_posted = db.Column(db.Date)

    author_user = db.relationship(User)
    author_org = db.relationship(Organization)

    def __init__(self, content, date_posted, author_user, author_org):
        self.content = content
        self.author_user = author_user
        self.date_posted = date_posted
        if author_org:
            self.author_org = author_org
        else:
            self.author_org = Organization.none()
        self.comments = []
