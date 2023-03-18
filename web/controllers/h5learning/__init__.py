from flask import Blueprint, render_template

route_h5learning = Blueprint('h5learning_page', __name__)

from web.controllers.h5learning.picslider import *
from web.controllers.h5learning.rotationmenu import *
from web.controllers.h5learning.bottomfish import *
from web.controllers.h5learning.rotationUI import *
from web.controllers.h5learning.morningandnight import *
from web.controllers.h5learning.flasfUI import *
from web.controllers.h5learning.themeslider import *
from web.controllers.h5learning.simplecard import *
from web.controllers.h5learning.travelpage import *
from web.controllers.h5learning.markdown import *

@route_h5learning.route('/')
def index():
    return render_template("h5learning/index.html")
