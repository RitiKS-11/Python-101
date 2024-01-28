from flask import Blueprint, render_template, request, make_response

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
    global count
    is_count_present = request.cookies.get('Count')
    count = int(is_count_present) + 1 if is_count_present else 1

    res = make_response(render_template('pages/count.html', count=count))
    res.set_cookie('Count', str(count))

    return res


