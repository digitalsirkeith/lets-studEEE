from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired, Email, InputRequired
from wtforms.widgets import TextArea

class JoinOrgForm(FlaskForm):
    id = HiddenField('id', validators=[DataRequired()])

class CreateOrgForm(FlaskForm):
    # TODO: Add photo_url
    name = StringField('name', validators=[DataRequired(), InputRequired()])
    email = StringField('email', validators=[DataRequired(), Email(), InputRequired()])
    description = StringField('description', widget=TextArea(), validators=[DataRequired()])

class EditOrgForm(FlaskForm):
    # TODO: Add photo_url
    description = StringField('description', widget=TextArea(), validators=[DataRequired()])
