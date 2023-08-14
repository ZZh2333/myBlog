from flask import render_template
from . import route_blog

@route_blog.route('/mysql')
def mysql():
    return render_template('/blog/mysql.html')