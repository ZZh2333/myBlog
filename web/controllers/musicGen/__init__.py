from flask import Blueprint,render_template

route_musicGen = Blueprint('musicGen_page',__name__)

from web.controllers.musicGen.api import *
from web.controllers.musicGen.musicgen import *

@route_musicGen.route('/',methods=["Get","POST"])
def index():
    return render_template('musicGen/index.html')