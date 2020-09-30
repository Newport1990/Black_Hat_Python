#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2020/9/29 12:22
# @Author : Newport
# @Site :
# @File : P2_2_UDP_Server.py
# @Software: PyCharm

import socket

target_host="10.211.55.4"
target_port=80

#建立一个socket对象
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#发送一些数据
client.sendto("AAABBBCCC",(target_host,target_port))

#接受一些数据

data,addr=client.recvfrom(4096)

print "输出结果："
print data