from flask import render_template
from . import route_h5learning

@route_h5learning.route('/markdown')
def markddown():
    return render_template('h5learning/markdown.html')