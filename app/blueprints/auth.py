from flask import Blueprint, render_template, flash, url_for, redirect
from flask_login import login_user, logout_user, login_required
from app.models.user import User, Role
from app.forms.auth import LoginForm, SignupForm
from app import db

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=('POST',))
def login():
    login_form = LoginForm()

    if login_form.validate():
        user = User.query.filter(User.email == login_form.email.data).one_or_none()

        if user is None:
            flash('Email is not registered to a user!', 'error')
        elif not user.check_password(login_form.password.data):
            flash('Incorrect password!', 'error')
        else:
            login_user(user)
    return redirect(url_for('root.root'))

@login_required
@bp.route('/logout', methods=('GET',))
def logout():
    logout_user()
    return redirect(url_for('root.root'))

@bp.route('/signup', methods=('POST',))
def signup():
    signup_form = SignupForm()

    if signup_form.validate():
        user_from_email = User.query.filter(User.email == signup_form.email.data).one_or_none()
        user_from_username = User.query.filter(User.username == signup_form.username.data).one_or_none()

        if user_from_email:
            flash('Email is already registed to another user!', 'error')
        elif user_from_username:
            flash('Username is already in use!', 'error')
        else:
            user = User(username=signup_form.username.data, 
                        email=signup_form.email.data,
                        password=signup_form.password.data,
                        contact_number=signup_form.contact_number.data)
            user_role = Role.query.filter(Role.name == 'user').one()
            user.roles.append(user_role)
            db.session.add(user)
            db.session.commit()
            login_user(user)
    return redirect(url_for('root.root'))