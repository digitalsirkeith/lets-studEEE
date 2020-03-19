from flask import Blueprint, render_template, request
from app import db
from ..models.user import User
from app.library import verify

bp = Blueprint('verify', __name__, url_prefix='/verify')

@bp.route('/username', methods=('GET',))
def username():
    if request.method == 'GET':
        username = request.args.get('username')
        if username is not None and User.query.filter(User.username == username).one_or_none() is None:
            return verify.available(True)
        else:
            return verify.available(False)