from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired, Email, InputRequired
from wtforms.widgets import TextArea

class JoinOrgForm(FlaskForm):
    id = HiddenField('id', validators=[DataRequired()])

class CreateOrgForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), InputRequired()])
    email = StringField('email', validators=[DataRequired(), Email(), InputRequired()])
    description = StringField('description', widget=TextArea(), validators=[DataRequired()])
    photo = FileField('image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])

class EditOrgForm(FlaskForm):
    description = StringField('description', widget=TextArea(), validators=[DataRequired()])
    photo = FileField('image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
