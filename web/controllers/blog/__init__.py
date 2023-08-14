from flask import Blueprint,render_template, request
import pandas as pd

route_blog = Blueprint('blog_page',__name__)

# from web.controllers.blog.steamcmdinstall import *
# from web.controllers.blog.maoxiandao import *
# from web.controllers.blog.mysql import *
# from web.controllers.blog.shellbash import *

@route_blog.route('/',methods=["Get","POST"])
def index():

    data = pd.read_csv('web/static/blog/csv/flod.csv')
    data['Date'] = pd.to_datetime(data['Date'])
    data['Year'] = data.Date.apply(lambda x: x.year)
    data['Month'] = data.Date.apply(lambda x: x.month)
    data['Day'] = data.Date.apply(lambda x: x.day)
    data = data.sort_values(by='Date',ascending=False)
    # print(data)
    rs = []
    for index,row in data.iterrows():
        rs.append(row)

    wanted = request.args.get("wanted", type=str)
    if wanted:
        # print("/blog/{}.html"%str(wanted))
        return render_template("/blog/{}.html".format(wanted),rs = rs)
    return render_template('blog/index.html',rs = rs)