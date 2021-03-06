#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2020/9/30 11:22
# @Author : Newport
# @Site :
# @File : P2_2_UDP_Server.py
# @Software: PyCharm

import socket
import threading

bind_ip="0.0.0.0"
bind_port=9999

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(5)

print "[*]listening on %s:%d" %(bind_ip,bind_port)

#这是客户处理线程
def handle_client(client_socket):
    #打印出客户端发送得到内容
    request=client_socket.recv(1024)
    print "[*] Received:%s"%request

    #返还一个数据包
    client_socket.send("ACK!")
    client_socket.close()

while True:
    client,addr=server.accept()
    print "[*] Accepted connection from:%s:%d" %(addr[0],addr[1])
    #挂起客户端线程，处理传入的数据
    client_handler=threading.Thread(target=handle_client,args=(client,))
    client_handler.start()

