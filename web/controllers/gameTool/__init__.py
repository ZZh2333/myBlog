from flask import Blueprint,render_template

route_gameTool = Blueprint('gameTool_page',__name__)

from . import soulMask

@route_gameTool.route('/',methods=['get','post'])
def index():
    # print("im here")
    return render_template('gameTool/index.html')