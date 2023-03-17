from . import route_h5learning
from flask import render_template

@route_h5learning.route('/travelpage')
def travelpage():
    return render_template('/h5learning/travelpage.html')