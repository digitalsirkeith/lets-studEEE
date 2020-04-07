from flask import Blueprint, render_template, request, session, flash, url_for, redirect
from flask_login import login_required, current_user
from app.forms.org import *
from app.models.org import Organization, OrganizationStatus, OrganizationRank, OrganizationUser
from app import db

bp = Blueprint('org', __name__, url_prefix='/org')

@bp.route('/', methods=('GET',))
@login_required
def home():
    return render_template('org/home.html', user=current_user, status=OrganizationStatus, rank=OrganizationRank)

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
                photo_url='',
                description=create_org_form.description.data
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

@bp.route('/edit/<int:id>', methods=('GET', 'POST'))
@login_required
def edit(id):
    edit_org_form = EditOrgForm()
    organization = Organization.query.get(id)

    if request.method == 'GET':
        if organization:
            edit_org_form.description.data = organization.description
            return render_template('org/edit.html', user=current_user, organization=organization, form=edit_org_form)
        else:
            flash('Org not found!', 'error')
            return redirect(url_for('org.home'))
    else:
        if edit_org_form.validate():
            if organization:
                organization.description = edit_org_form.description.data
                db.session.commit()
            else:
                flash('Org not found!', 'error')
        return redirect(url_for('org.home'))

@bp.route('/view/<int:id>', methods=('GET',))
@login_required
def view(id):
    organization = Organization.query.get(id)
    if organization:
        association = OrganizationUser.query.get((current_user.id, id))
        if association:
            return render_template('org/view.html', user=current_user, organization=organization, rank=association.rank)
        else:
            return render_template('org/view.html', user=current_user, organization=organization, rank='')
    else:
        flash('Org not found!', 'error')
        return redirect(url_for('org.home'))