from flask import Blueprint, render_template

route_index = Blueprint('index_page',__name__)


@route_index.route('/')
def myindex():
    return render_template("index/myindex.html")
    # return render_template("blog/index.html")


@route_index.route('/index')
def index():
    return render_template("index/index.html")