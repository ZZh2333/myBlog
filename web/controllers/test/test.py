from flask import render_template, Blueprint

route_test = Blueprint('test_page', __name__)


@route_test.route('/')
def test():
    return render_template("test/test.html")

@route_test.route('/test2')
def test2():
    return render_template("test/test2.html")
