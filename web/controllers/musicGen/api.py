from . import route_musicGen
from flask import request, render_template, jsonify, redirect
import os
from datetime import timedelta
import json

@route_musicGen.route('/api')
def api():
    ans = 'zzh1'
    return ans

@route_musicGen.route('/upload', methods=['POST', 'GET'])
def upload():
    # print("222")
    if request.method == 'POST':
        # 通过file标签获取文件
        f = request.files['img']
        # if not (f and allowed_file(f.filename)):
        #     return jsonify({"error": 1001, "msg": "图片类型：png、PNG、jpg、JPG、bmp"})
        # 当前文件所在路径
        basepath = os.path.dirname(__file__)
        # print(basepath)
        # 一定要先创建该文件夹，不然会提示没有该路径
        upload_path = os.path.join(basepath, '../../static/musicGen/music/img', '1.jpg')
        # 保存文件
        print(upload_path)
        f.save(upload_path)
        # 返回上传成功界面
        return json.dumps("success"),200,{'Content-Type':'application/json'}
    # 重新返回上传界面
    return json.dumps("success"),200,{'Content-Type':'application/json'}