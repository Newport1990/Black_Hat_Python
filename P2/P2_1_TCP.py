#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2020/9/29 11:52
# @Author : Newport
# @Site :
# @File : P2_2_UDP_Server.py
# @Software: PyCharm


import socket


#target_host = "www.baidu.com"
#target_port = 80

target_host = "127.0.0.1"
target_port = 9999

#建立一个socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接客户端
client.connect((target_host, target_port))

# 发送一些数据
#client.send("GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n")
client.send("ABCDEF\n")

# 接受一些数据
response = client.recv(4096)

print '输出结果：'
print response
