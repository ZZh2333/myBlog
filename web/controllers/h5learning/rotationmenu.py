from . import route_h5learning
from flask import render_template

@route_h5learning.route('/rotationmenu')
def rotationmenu():
    return render_template("h5learning/rotationmenu.html")