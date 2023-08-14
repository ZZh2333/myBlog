from flask import render_template
from . import route_blog

@route_blog.route('/steamcmdinstall')
def steamcmdinstall():
    return render_template('/blog/steamcmdinstall.html')