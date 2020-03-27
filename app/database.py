from flask.cli import with_appcontext
from app.models.user import User, Role
from app.models.org import Organization
from app import db
import click
import os

def create_user_role():
    if Role.query.filter(Role.name == 'user').one_or_none() is None:
        user_role = Role('user')
        db.session.add(user_role)
        db.session.commit()

def create_admin_role():
    if Role.query.filter(Role.name == 'admin').one_or_none() is None:
        admin_role = Role('admin')
        db.session.add(admin_role)
        db.session.commit()

def create_admin_account():
    admin_username = os.getenv('ADMIN_USERNAME')
    admin_email = os.getenv('ADMIN_EMAIL')
    admin_contact = os.getenv('ADMIN_CONTACT')
    admin_password = os.getenv('ADMIN_PWD')
    if User.query.filter(User.username == admin_username).one_or_none() is None:

        admin_role = Role.query.filter(Role.name == 'admin').one()
        user_role = Role.query.filter(Role.name == 'user').one()

        admin = User(admin_username, admin_email, admin_password, admin_contact)
        admin.roles.append(admin_role)
        admin.roles.append(user_role)

        db.session.add(admin)
        db.session.commit()

def create_no_org():
    if Organization.none() is None:
        no_org = Organization(name='no_org', email=None, owner=None, photo_url=None)
        db.session.add(no_org)
        db.session.commit()

@click.command('init-db')
@with_appcontext
def init_db_command():
    create_user_role()
    create_admin_role()
    create_admin_account()
    create_no_org()

    click.echo('Initialized users.')

def init_app(app):
    app.cli.add_command(init_db_command)