from flask import Blueprint, render_template, request
import redis

bp = Blueprint("pages", __name__)
redis_client = redis.Redis(host='localhost', port='6379')


@bp.route("/")
def home():
    return render_template('pages/home.html')


@bp.route("/about")
def about():
    return render_template('pages/about.html')


@bp.route('/visit')
def visit_count():
    user_ip = request.remote_addr
    count = 0

    if redis_client.exists(user_ip):
        count = int(redis_client.get(user_ip)) + 1
        redis_client.set(user_ip, count)
    else:
        redis_client.set(user_ip, count)


    return render_template('pages/count.html', count=count)

