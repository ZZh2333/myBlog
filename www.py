from application import app
from web.controllers.index import route_index
from web.controllers.static import route_static

from web.controllers.test.test import route_test

app.register_blueprint(route_index,url_prefix='/')
app.register_blueprint(route_static, url_prefix="/static")

app.register_blueprint(route_test,url_prefix="/test")