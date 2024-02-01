from flask import Flask

from board import pages, errors

def create_app():
    app = Flask(__name__)
    app.secret_key = 'example'
    app.register_blueprint(pages.bp)
    app.register_error_handler(404, errors.page_not_found)

    return app