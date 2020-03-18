from flask import Blueprint, render_template, request
from ..models.user import User

bp = Blueprint('home', __name__)

@bp.route('/', methods=('GET',))
def home():
    if request.method == 'GET':
        return render_template('home.html')