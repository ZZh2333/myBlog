from . import route_h5learning
from flask import render_template

@route_h5learning.route('/simplecard')
def sample():
    return render_template('/h5learning/simplecard.html')