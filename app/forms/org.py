from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired, Email, InputRequired

class JoinOrgForm(FlaskForm):
    id = HiddenField('id', validators=[DataRequired()])

class CreateOrgForm(FlaskForm):
    # TODO: Add description and photo_url
    name = StringField('name', validators=[DataRequired(), InputRequired()])
    email = StringField('email', validators=[DataRequired(), Email(), InputRequired()])

class EditOrgForm(FlaskForm):
    # TODO: Add description and photo_url
    pass

class DeleteOrgForm(FlaskForm):
    # do we need this?
    id = HiddenField('id', validators=[DataRequired()])