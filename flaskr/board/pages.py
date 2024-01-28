from flask import Blueprint, render_template

bp = Blueprint("pages", __name__)

count = 0

@bp.route("/")
def home():
    return render_template('pages/home.html')

@bp.route("/about")
def about():
    return render_template('pages/about.html')

@bp.route('/visit')
def visit_count():
    count = counter()
    return render_template('pages/count.html', count=count)


def counter():
    global count
    count += 1
    return count