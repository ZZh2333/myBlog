from flask import Blueprint, render_template

route_h5learning = Blueprint('h5learning_page', __name__)

from web.controllers.h5learning.picslider import *
from web.controllers.h5learning.rotationmenu import *
from web.controllers.h5learning.bottomfish import *
from web.controllers.h5learning.rotationUI import *


@route_h5learning.route('/')
def index():
    return render_template("h5learning/index.html")
