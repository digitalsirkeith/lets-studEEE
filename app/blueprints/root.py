from flask import Blueprint, render_template, request, session
from flask_login import login_user
from ..models.user import User

bp = Blueprint('root', __name__)

@bp.route('/', methods=('GET','POST'))
def root():
    if request.method == 'GET':
        return render_template('root.html')
    else:
        if 'email' in request.form and 'password' in request.form:
            login_user(user)
        return render_template('root.html')