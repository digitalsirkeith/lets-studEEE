from app import db
from app.models.user import User
from app.models.org import Organization

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    author_user_id = db.Column(db.Integer, db.ForeignKey(User.id, ondelete='CASCADE'))
    author_org_id = db.Column(db.Integer, db.ForeignKey(Organization.id, ondelete='CASCADE'))
    datetime_posted = db.Column(db.DateTime)

    author_user = db.relationship(User, back_populates='posts')
    author_org = db.relationship(Organization, back_populates='posts')
    comments = db.relationship('Comment')
    study_session = db.relationship('StudySession', back_populates='post')

    def __init__(self, title, content, datetime_posted, author_user, author_org):
        self.title = title
        self.content = content
        self.author_user = author_user
        self.datetime_posted = datetime_posted
        if author_org:
            self.author_org = author_org
        else:
            self.author_org = Organization.none()
        self.comments = []

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    author_user_id = db.Column(db.Integer, db.ForeignKey(User.id, ondelete='CASCADE'))
    author_org_id = db.Column(db.Integer, db.ForeignKey(Organization.id, ondelete='CASCADE'))
    post_id = db.Column(db.Integer, db.ForeignKey(Post.id, ondelete='CASCADE'))
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
