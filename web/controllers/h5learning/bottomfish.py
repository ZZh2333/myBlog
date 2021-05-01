from . import route_h5learning
from flask import render_template

@route_h5learning.route('/bottomfish')
def bottomfish():
    return render_template('h5learning/bottomfish.html')