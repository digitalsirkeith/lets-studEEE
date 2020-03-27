from flask import Blueprint, render_template, request, session, flash, url_for, redirect
from flask_login import login_required, current_user
# from app import db

bp = Blueprint('org', __name__, url_prefix='/org')

@bp.route('/', methods=('GET',))
@login_required
def home():
    return render_template('study/org/home.html', user=current_user)

@bp.route('/create', methods=('GET',))
@login_required
def create():
    flash('Create not implemented yet', 'error')
    return redirect(url_for('org.home'))
    return render_template('study/org/create.html', user=current_user)

@bp.route('/join', methods=('GET',))
@login_required
def join():
    flash('Join not implemented yet', 'error')
    return redirect(url_for('org.home'))
    return render_template('study/org/join.html', user=current_user)



# new study session