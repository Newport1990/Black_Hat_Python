#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2020/9/30 15:22
# @Author : Newport
# @Site : 
# @File : netcat_client.py
# @Software: PyCharm


import sys
import socket
import getopt
import threading
import subprocess

#定义一些全局变量
listen  =False
command =False
upload  =False
execute =""
target  =""
upload_destination =""
port    =0

def usage():
    print "BHP Net Tool"
    print
    print "Usage:bhpnet.py -t target_host -p port"
    print "-l --listen"    - listen on [host]:[port] for incoming connections"
    print "-e --excute=file_to_run   - execute the given file upon receiving a connection"
    print "-c --command   -initialize a command shell"
    print "-u --upload=destination   --upon receiving connection upload a file and write to [destination]"
    print
    print
    print "Examples:"
    print "bhpnet.py -t 192.168.0.1 -p 5555 -l -c"
    print "bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe"
    print "bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\""
    sys.exit(0)

def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()
    #读取命令行选项
    try:
        opts,args=getopt.getopt(sys.argv[1:],"hle:t:p:cu",["help","listen","execute","target","port","command","upload"])
    except getopt.GetoptError as err:
        usage()

    for o,a in opts:
        if o in ("-h","--help"):
            usage()
        elif o in ("-l","--listen"):
            listen=True
        elif o in ("-e","--execute"):
            execute=a
        elif o in ("-c","--command"):
            command=True
        elif o in ("-u","--upload"):
            upload_destination=a
        elif o in ("-t","--target"):
            target=a
        elif o in ("-p","--port"):
            port=int(a)
        else:
            assert False,"Unhandle Option"

        #我们是进行监听还是仅从标准输入发送数据
        if not listen and len(target) and port>0:
            #从命令行读取内存数据
            #这里将阻塞，所以不在向标准输入发送数据时发送CTRL -D
            buffer=sys.stdin.read()

            #发送数据
            client_sender(buffer)

        #我们开始监听并准备上传文件，执行命令
        #放置一个反弹shell
        #取决于上面的命令行选项
        if listen:
            server_loop()

main()