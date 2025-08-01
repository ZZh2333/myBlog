#!/bin/bash


conda activate myblog
# 检查是否安装了 Python 和 pip
if ! command -v python3 &> /dev/null; then
    echo "Python3 未安装，请先安装 Python3。"
    exit 1
fi

if ! command -v pip3 &> /dev/null; then
    echo "pip3 未安装，正在安装 pip3..."
    sudo apt-get update
    sudo apt-get install -y python3-pip
fi

# 创建虚拟环境
echo "创建虚拟环境..."
python3 -m venv venv

# 激活虚拟环境
echo "激活虚拟环境..."
source venv/bin/activate

# 安装依赖
if [ -f "requirements.txt" ]; then
    echo "正在安装依赖..."
    pip3 install -r requirements.txt
else
    echo "未找到 requirements.txt 文件，请确保文件存在。"
    exit 1
fi

echo "依赖安装完成！"
