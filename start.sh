#!/bin/bash

while true; do
    # 运行 ping-zkitefly.py 脚本
    python3 ping-zkitefly.py

    # 等待一段时间后重新运行脚本
    echo "Script stopped. Restarting in 10 secs..."
    sleep 10
done