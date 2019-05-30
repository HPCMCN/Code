#!/bin/bash
base_dir=$(dirname $(readlink -f "$0"))
script=manager.py

function start(){
    if ps -aux | grep $script | grep -v grep >> /dev/null
    then
        echo "服务正在运行!"
    else
        nohup python -u $base_dir/$script runserver -h 0.0.0.0 -p 5000  >> $base_dir/logs/nohup.log 2>&1 & echo $! > .pid
        if [ $? == 0 ]
        then
            if  ps -ef | grep $script | grep -v grep >/dev/null
            then
                echo "服务启动成功!"
            else
                echo "服务启动失败!"
            fi
        else
            echo "服务启动失败!"
        fi
    fi
}

function stop(){
    if ps -aux | grep $script | grep -v grep >> /dev/null
    then
        ps -aux | grep manager.py | grep -v grep | awk '{print $2}' | xargs kill -9 >> /dev/null
        if [ $? == 0 ]
        then
            echo "服务已关闭!"
        else
            echo "服务关闭失败!"
        fi
    else
        echo "服务未启用!"
    fi
}

function log(){
    log_path=$base_dir/logs/nohup.log
    cat $log_path &&
    tail -f $log_path
}


function main(){
    read -p $'1. 启动\n2. 停止\n3. 当前输出\n0. 退出\n请输入:' e
    case $e in
        1)
            start
            ;;
        2)
            stop
            ;;
        3)
            log
            ;;
        0)
            return 22
            ;;
        *)
            echo "选择错误!"
            ;;
    esac
}

while true
do
    main
    if [ $? == 22 ]
    then
        echo "脚本退出!"
        break
    fi
done
