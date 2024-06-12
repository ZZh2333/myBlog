from flask import render_template,request,jsonify
from . import route_gameTool
import winrm,os
import configparser

@route_gameTool.route('/soulMask',methods=['get','post'])
def soulMask():
    if request.json:

        data = request.json
        IP = data.get('IP')
        user = data.get('user')
        passwd = data.get('passwd')
        currentDate = data.get('currentDate')

        # 处理接收到的数据
        print(f'Received input 1: {IP}')
        print(f'Received input 2: {user}')
        print(f'Received input 3: {passwd}')
        print(f'Received input 3: {currentDate}')
 
        # 创建配置解析器
        config_file_path = 'config/gameTool/conf.ini'
        # 检查配置文件是否存在
        if not os.path.isfile(config_file_path):
            raise FileNotFoundError(f"Configuration file '{config_file_path}' not found.")
        config = configparser.ConfigParser()

        config.read(config_file_path)
        auth = config['gameTool settings']['auth']

        if passwd == auth:
            session = winrm.Session('http://47.108.165.146:5985/wsman',auth=('Administrator','Zouzihan0706'))

            # 停止游戏
            process_name = 'WSServer-Win64-Shipping'
            ps_script = f"Stop-Process -Name '{process_name}'"
            result = session.run_ps(ps_script)
            if result.status_code == 0:
                print(f"Process '{process_name}' stoped successfully.")
            else:
                print(f"Failed to stop process '{process_name}'.")
                print(f"Error: {result.std_err.decode()}")
            
            # 更新游戏
            session = winrm.Session('http://47.108.165.146:5985/wsman',auth=('Administrator','Zouzihan0706'))
            steamcmd_script_path = "C:\\Users\\Administrator\\Desktop\\steamcmd_script.ps1"
            ps_script = f"& '{steamcmd_script_path}'"
            result = session.run_ps(ps_script)
            # 检查执行结果
            if result.status_code == 0:
                print("SteamCMD commands executed successfully.")
                # print(result.std_out.decode())
            else:
                print("Failed to execute SteamCMD commands.")
                # print(f"Error: {result.std_err.decode()}")

            # 启动游戏
            session = winrm.Session('http://47.108.165.146:5985/wsman',auth=('Administrator','Zouzihan0706'))
            bat_file_path = "C:\\Users\\Administrator\\Desktop\\steamcmd\\steamcmd\\steamapps\\common\\Soulmask Dedicated Server For Windows\\StartServer.bat" 
            ps_command = f'Start-Process -FilePath "{bat_file_path}" -NoNewWindow'
            result = session.run_ps(ps_command)
            # if result.status_code == 0:
            #     print("Batch script started successfully and is running in the background.")
            # else: 
            #     print("Failed to start the batch script.")
            #     print(f"Error: {result.std_err.decode()}")
            # print(result.status_code)

        return render_template('/gameTool/soulMask.html')

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