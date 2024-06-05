from flask import render_template,request,jsonify
from . import route_gameTool
import winrm

@route_gameTool.route('/soulMask',methods=['get','post'])
def soulMask():
    if request.json:

        data = request.json
        IP = data.get('IP')
        user = data.get('user')
        passwd = data.get('passwd')

        # 处理接收到的数据
        print(f'Received input 1: {IP}')
        print(f'Received input 2: {user}')
        print(f'Received input 3: {passwd}')

    # action = request.args.get("action",type=str)
    # if action == 'restart':
    #     server = "http://47.108.165.146:5985/wsman"
    #     username = 'Administrator'
    #     password = 'Zouzihan0706'

    #     session = winrm.Session(server,auth=(username,password))

    #     process_name = 'WSServer-Win64-Shipping.exe'
    #     command = f'taskkill /F /IM {process_name}'

    #     result = session.run_cmd(command)
    #     print(result.status_code)
    #     print(result.std_out.decode())
    #     print(result.std_err.decode())
    return render_template('/gameTool/soulMask.html')