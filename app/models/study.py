from app import db
from app.models.feed import Post
from app.models.user import User

class Topic(db.Model):
    __tablename__ = 'topics'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    
    study_sessions = db.relationship('StudySession', secondary='study_session_topics')

    def __init__(self, name):
        self.name = name

class StudySession(db.Model):
    __tablename__ = 'study_sessions'

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey(Post.id, ondelete='CASCADE'))
    schedule_start = db.Column(db.DateTime)
    finished = db.Column(db.Boolean)

    post = db.relationship(Post, back_populates='study_session')
    topics = db.relationship(Topic, secondary='study_session_topics')
    members = db.relationship(User, secondary='study_session_members')
    ratings = db.relationship('StudySessionRating', back_populates='study_session')

    def __init__(self, schedule_start, post, topic_names=[]):
        self.schedule_start = schedule_start
        self.finished = False
        self.post = post

        for topic_name in topic_names:
            topic = Topic.query.filter(Topic.name == topic_name).one_or_none()

            if topic is None:
                topic = Topic(topic_name)
                db.session.add(topic)
                db.session.commit()

            self.topics.append(topic)

class StudySessionRating(db.Model):
    __tablename__ = 'study_session_ratings'

    author_id = db.Column(db.Integer, db.ForeignKey(User.id, ondelete='CASCADE'), primary_key=True)
    study_session_id = db.Column(db.Integer, db.ForeignKey(StudySession.id, ondelete='CASCADE'), primary_key=True)
    rating = db.Column(db.Integer)
    content = db.Column(db.Text)

    author = db.relationship(User)
    study_session = db.relationship(StudySession, back_populates='ratings')

    def __init__(self, author, study_session, rating, content):
        self.author = author
        self.study_session = study_session
        self.rating = rating
        self.content = content

class StudySessionTopic(db.Model):
    __tablename__ = 'study_session_topics'

    topic_id = db.Column(db.Integer, db.ForeignKey(Topic.id, ondelete='CASCADE'), primary_key=True)
    study_session_id = db.Column(db.Integer, db.ForeignKey(StudySession.id, ondelete='CASCADE'), primary_key=True)

class StudySessionMembers(db.Model):
    __tablename__ = 'study_session_members'

    study_session_id = db.Column(db.Integer, db.ForeignKey(StudySession.id, ondelete='CASCADE'), primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey(User.id, ondelete='CASCADE'), primary_key=True)