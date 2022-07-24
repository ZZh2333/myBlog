from . import route_h5learning
from flask import render_template

@route_h5learning.route('/themeslider')
def themeslider():
    return render_template('/h5learning/themeslider.html')