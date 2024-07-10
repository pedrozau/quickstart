# create route here
from flask import render_template


def init_routes(app):

    # create the route 
    @app.route('/')
    def index():
        return render_template('index.html')