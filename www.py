from application import app
from web.controllers.index import route_index
from web.controllers.static import route_static

from web.controllers.test.test import route_test
from web.controllers.h5learning import route_h5learning
from web.controllers.h5game import route_h5game
from web.controllers.blog import route_blog

app.register_blueprint(route_index,url_prefix='/')
app.register_blueprint(route_static, url_prefix="/static")

app.register_blueprint(route_test,url_prefix="/test")
app.register_blueprint(route_h5learning,url_prefix="/h5learning")
app.register_blueprint(route_h5game,url_prefix="/h5game")
app.register_blueprint(route_blog,url_prefix='/blog')