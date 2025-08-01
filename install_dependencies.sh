#!/bin/bash

source ~/.bashrc
conda activate myblog
# 检查是否安装了 Python 和 pip
if ! command -v python &> /dev/null; then
    echo "python 未安装，请先安装 python。"
    exit 1
fi

if ! command -v pip &> /dev/null; then
    echo "pip 未安装，正在安装 pip..."
    sudo apt-get update
    sudo apt-get install -y python-pip
fi

# 安装依赖并跳过 @ 后目录不存在的报错
if [ -f "requirements.txt" ]; then
    echo "正在安装依赖..."
    pip install --ignore-installed --no-deps -r requirements.txt
else
    echo "未找到 requirements.txt 文件，请确保文件存在。"
    exit 1
fi

echo "依赖安装完成！"
