from flask import Blueprint,render_template
import pandas as pd

route_blog = Blueprint('blog_page',__name__)

from web.controllers.blog.steamcmdinstall import *
from web.controllers.blog.maoxiandao import *

@route_blog.route('/',methods=["Get","POST"])
def index():
    data = pd.read_csv('web/static/blog/csv/flod.csv')
    data['Date'] = pd.to_datetime(data['Date'])
    data['Month'] = data.Date.apply(lambda x: x.month)
    data['Day'] = data.Date.apply(lambda x: x.day)
    data = data.sort_values(by='Date',ascending=False)
    # print(data)
    rs = []
    for index,row in data.iterrows():
        rs.append(row)
    return render_template('blog/index.html',rs = rs)