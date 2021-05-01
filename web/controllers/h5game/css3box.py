from . import route_h5game
from flask import render_template

@route_h5game.route('/css3box')
def css3box():
    return render_template('/h5game/css3box.html')