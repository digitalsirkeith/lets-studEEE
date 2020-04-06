from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, HiddenField, RadioField
from wtforms.validators import DataRequired, Email, InputRequired, EqualTo
from wtforms.widgets import TextArea

class CreateStudySessionForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(), InputRequired()])
    content = StringField('content', widget=TextArea(), validators=[DataRequired(), InputRequired()])
    method = SelectField('method', coerce=int, validators=[DataRequired()])
    topic_names = StringField('topic_names', validators=[DataRequired()])

class JoinStudySessionForm(FlaskForm):
    id = HiddenField('id', validators=[DataRequired()])

class EditStudySessionForm(FlaskForm):
    id = HiddenField('id', validators=[DataRequired()])
    title = StringField('title', validators=[DataRequired(), InputRequired()])
    content = StringField('content', widget=TextArea(), validators=[DataRequired(), InputRequired()])
    topic_names = StringField('topic_names', validators=[DataRequired()])

class AddStudySessionRatingForm(FlaskForm):
    study_session_id = HiddenField('study_session_id')
    content = StringField('content', widget=TextArea(), validators=[DataRequired()])
    rating = RadioField('rating', choices=[1,2,3,4,5], validators=[DataRequired()])