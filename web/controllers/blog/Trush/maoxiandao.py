from flask import render_template
from . import route_blog

@route_blog.route('/maoxiandao')
def maoxiandao():
    return render_template('/blog/maoxiandao.html')