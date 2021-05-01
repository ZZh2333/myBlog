from . import route_h5learning
from flask import render_template

@route_h5learning.route('/rotationUI')
def rotationUI():
    return render_template('/h5learning/rotationUI.html')