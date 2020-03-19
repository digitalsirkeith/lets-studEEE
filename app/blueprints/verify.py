from flask import Blueprint, render_template, request
from app import db
from ..models.user import User
from app.library import verify

bp = Blueprint('verify', __name__, url_prefix='/verify')

@bp.route('/', methods=('GET',))
def username():
    if request.method == 'GET':
        username = request.args.get('username')
        email = request.args.get('email')
        email_available = False
        username_available = False

        if username is not None and User.query.filter(User.username == username).one_or_none() is None:
            username_available = True
        if email is not None and User.query.filter(User.email == email).one_or_none() is None:
            email_available = True

        return verify.available(email_available, username_available)