from flask import Blueprint, render_template, request, session, flash, url_for, redirect
from flask_login import login_required, current_user
from app import db

bp = Blueprint('study', __name__, url_prefix='/study')

@bp.route('/', methods=('GET',))
@login_required
def home():
    return redirect(url_for('study.show'))

@bp.route('/show', methods=('GET',))
@login_required
def show():
    return render_template('study/show.html', user=current_user)

@bp.route('/create', methods=('GET','POST'))
@login_required
def create():
    return render_template('study/create.html', user=current_user)

@bp.route('/edit/<int:id>', methods=('GET','POST'))
@login_required
def edit(id):
    return render_template('study/edit.html', user=current_user)

@bp.route('/view/<int:id>', methods=('GET',))
@login_required
def view(id):
    return render_template('study/view.html', user=current_user)
