from flask import Blueprint,render_template

route_blog = Blueprint('blog_page',__name__)

from web.controllers.blog.steamcmdinstall import *

@route_blog.route('/')
def index():
    return render_template('blog/index.html')