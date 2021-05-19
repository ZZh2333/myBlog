from . import route_h5learning
from flask import render_template

@route_h5learning.route('/morningandnight')
def morningandnight():
    return render_template('h5learning/morningandnight.html')