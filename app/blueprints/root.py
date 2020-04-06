from flask import Blueprint, render_template
from flask_login import login_user, current_user
from app.models.user import User
from app.forms.auth import LoginForm, SignupForm

bp = Blueprint('root', __name__)

@bp.route('/', methods=('GET',))
def root():
    if current_user.is_authenticated:
        return render_template('home.html', user=current_user)
    else:
        return render_template('root.html', login_form=LoginForm(), signup_form=SignupForm(), user=current_user)