from flask import Blueprint, render_template, request
import pandas as pd

route_index = Blueprint('index_page',__name__)


@route_index.route('/',methods=['Get','POST'])
def myindex():
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
    # return render_template("index/myindex.html",rs = rs)
        wanted = request.args.get("wanted", type=str)
    if wanted:
        # print("/blog/{}.html"%str(wanted))
        return render_template("/blog/{}.html".format(wanted),rs = rs)
    return render_template("blog/index.html",rs = rs)


@route_index.route('/index')
def index():
    return render_template("index/index.html")