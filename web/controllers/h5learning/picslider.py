from . import route_h5learning
from flask import render_template

@route_h5learning.route('/picslider')
def picslider():
    return render_template('h5learning/picslider.html')