from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, HiddenField
from wtforms.validators import DataRequired, Email, InputRequired, EqualTo
from wtforms.widgets import TextArea

class CreatePostForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(), InputRequired()])
    content = StringField('content', widget=TextArea(), validators=[DataRequired(), InputRequired()])
    method = SelectField('method', coerce=int, validators=[DataRequired()])

class EditPostForm(FlaskForm):
    id = HiddenField('id', validators=[DataRequired()])
    title = StringField('title', validators=[DataRequired(), InputRequired()])
    content = StringField('content', widget=TextArea(), validators=[DataRequired(), InputRequired()])

class DeletePostForm(FlaskForm):
    id = HiddenField('id', validators=[DataRequired()])

class AddCommentForm(FlaskForm):
    post_id = HiddenField('post_id', validators=[DataRequired()])
    content = StringField('content', validators=[DataRequired(), InputRequired()])

class EditCommentForm(FlaskForm):
    id = HiddenField('id', validators=[DataRequired()])
    content = StringField('content', validators=[DataRequired(), InputRequired()])

class DeleteCommentForm(FlaskForm):
    id = HiddenField('id', validators=[DataRequired()])
