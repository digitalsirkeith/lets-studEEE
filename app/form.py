from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, InputRequired, EqualTo

class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()]) 
    password = PasswordField('password', validators=[DataRequired()])
    
class SignupForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email(), InputRequired()]) 
    username = StringField('username', validators=[DataRequired(), InputRequired()]) 
    password = PasswordField('password', validators=[DataRequired(), InputRequired(), 
                                EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('confirmpassword', validators=[DataRequired(), InputRequired()])
    contact_number = StringField('num', validators=[DataRequired(), InputRequired()])
    tc_checkbox = BooleanField('tc', validators=[DataRequired(), InputRequired()])