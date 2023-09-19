from . import route_h5learning
from flask import render_template

@route_h5learning.route('/pingip')
def pingip():
    return render_template('/h5learning/pingip.html')