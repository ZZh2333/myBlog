from flask import render_template
from . import route_blog


@route_blog.route('/shellbash')
def shellbash():
    return render_template('/blog/shellbash.html')