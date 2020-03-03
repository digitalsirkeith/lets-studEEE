from flask import Blueprint, render_template, request

bp = Blueprint('home', __name__)

@bp.route('/', methods=('GET',))
def home():
    if request.method == 'GET':
        return render_template('home.html')