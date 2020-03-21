from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms.validators import DataRequired, InputRequired, EqualTo

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('old_password', validators=[DataRequired(), InputRequired()])
    new_password = PasswordField('new_password', validators=[DataRequired(), InputRequired(), 
                                EqualTo('confirm', message='Passwords must match')])
    confirm      = PasswordField('confirm', validators=[DataRequired(), InputRequired()])