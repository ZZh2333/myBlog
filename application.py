from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
import os
from common.libs.UrlManager import UrlManager 

class Application(Flask):
    def __init__(self,import_name,template_folder=None,root_path=None):
        super(Application,self).__init__(import_name,template_folder=template_folder,static_folder=None,root_path=root_path)
        self.config.from_pyfile('config/local_setting.py')
        
        # todo:按环境加载配置文件
        
        # db.__init__(self)



# db = SQLAlchemy()
app = Application(__name__,template_folder=os.getcwd()+'/web/templates',root_path=os.getcwd())

# 处理跨域问题
@app.after_request
def add_cors_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE,OPTIONS'
    return response

manager = Manager(app)

# 函数模板,使得在html中也可以调用python方法
app.add_template_global(UrlManager.buildStaticUrl, "buildStaticUrl")
app.add_template_global(UrlManager.buildUrl, "buildUrl")