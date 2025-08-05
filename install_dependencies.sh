#!/bin/bash

# 初始化conda环境
# if ! grep -q "conda initialize" ~/.bashrc; then
#     echo "请先运行 'conda init' 初始化环境"
#     exit 1
# fi

# 加载conda环境
. ~/.bashrc

# 检查conda环境
if ! conda env list | grep -q "myblog"; then
    echo "Conda环境'myblog'不存在，请先创建"
    exit 1
fi

# 激活conda环境
conda activate myblog

# 检查python（使用conda环境中的python）
# if ! python --version &> /dev/null; then
#     echo "Python未正确安装或conda环境有问题"
#     exit 1
# fi

# 安装依赖
while read requirement; do pip install --no-cache-dir $requirement || continue; done < requirements.txt

echo "依赖安装完成！"

echo "依赖安装完成！"
