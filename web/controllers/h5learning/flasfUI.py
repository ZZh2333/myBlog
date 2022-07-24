from . import route_h5learning
from flask import render_template

@route_h5learning.route('/flashUI')
def flashUI():
    return render_template('h5learning/flashUI.html')