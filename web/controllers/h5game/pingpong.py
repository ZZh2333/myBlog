from . import route_h5game
from flask import render_template

@route_h5game.route('/pingpong')
def pingpong():
    return render_template('/h5game/pingpong.html')