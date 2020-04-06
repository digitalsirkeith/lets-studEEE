from flask import Blueprint, render_template, request, session, flash, url_for, redirect
from flask_login import login_required, current_user
from app.forms.org import *
from app.models.org import Organization, OrganizationStatus
from app import db

bp = Blueprint('org', __name__, url_prefix='/org')

@bp.route('/', methods=('GET',))
@login_required
def home():
    return render_template('org/show.html', user=current_user, status=OrganizationStatus)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    create_org_form = CreateOrgForm()
    if request.method == 'GET':
        return render_template('org/create.html', user=current_user, form=create_org_form)
    else:
        if create_org_form.validate():
            new_org = Organization(
                name=create_org_form.name.data,
                email=create_org_form.email.data,
                owner=current_user,
                photo_url=''
            )
            
            db.session.add(new_org)
            db.session.commit()

            flash('New organization created! Wait for approval from the website administration', 'info')
            
        else:
            for _, messages in create_org_form.errors.items():
                flash('. '.join(messages), 'error')

        return redirect(url_for('org.home'))

@bp.route('/join', methods=('GET', 'POST'))
@login_required
def join():
    if request.method == 'GET':
        return render_template('org/join.html', user=current_user)
    else:
        return redirect(url_for('org.home'))

@bp.route('/edit', methods=('GET', 'POST'))
@login_required
def edit():
    if request.method == 'GET':
        return render_template('org/edit.html', user=current_user)
    else:
        return redirect(url_for('org.home'))