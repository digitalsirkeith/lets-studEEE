from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import logout_user, current_user, login_required
from app.models.user import User
from app.forms.changepw import ChangePasswordForm
from app import db

bp = Blueprint('changepw', __name__)

@bp.route('/changepw', methods=('GET','POST'))
@login_required
def root():
    changepw_form = ChangePasswordForm()
    if request.method == 'GET':
        return render_template('changepw.html', form=changepw_form, user=current_user)
    else:
        if changepw_form.validate():
            if current_user.check_password(changepw_form.old_password.data):
                current_user.set_password(changepw_form.new_password.data)
                db.session.commit()
                logout_user()
                flash('Password changed! You have been logged out.', 'info')
                return redirect(url_for('root.root'))
            else:
                flash('Incorrect password!', 'error')
        else:
            for _, messages in changepw_form.errors.items():
                flash('. '.join(messages), 'error')
        return redirect(url_for('changepw.root'))