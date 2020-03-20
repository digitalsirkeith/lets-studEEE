from flask import Blueprint, render_template, request, session, flash, url_for, redirect
from flask_login import login_user, logout_user
from app.models.user import User
from app.form import LoginForm, SignupForm

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=('POST',))
def login():
    login_form = LoginForm()

    if login_form.validate():
        user = User.query.filter(User.email == login_form.email.data).one_or_none()

        if user is None:
            flash('Email is not registered to a user!')
        elif not user.check_password(login_form.password.data):
            flash('Incorrect password!')
        else:
            login_user(user)
        return redirect(url_for('root.root'))

@bp.route('/logout', methods=('GET',))
def logout():
    logout_user()
    return redirect(url_for('root.root'))

@bp.route('/signup', methods=('POST',))
def signup():
    signup_form = SignupForm()
    flash('Signup not supported yet.')
    return redirect(url_for('root.root'))