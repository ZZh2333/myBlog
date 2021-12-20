from flask import Blueprint,render_template

route_h5game = Blueprint('h5game_page',__name__)

from .css3box import *
from .pingpong import *

@route_h5game.route('/')
def index():
    return render_template("h5game/index.html")