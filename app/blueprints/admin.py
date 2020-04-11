from flask import Blueprint, render_template, request, session, flash, url_for, redirect
from flask_login import login_required, current_user
from app import db

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/', methods=('GET',))
@login_required
def home():
    return redirect(url_for('root.root'))
    return render_template('forum/home.html', user=current_user)
