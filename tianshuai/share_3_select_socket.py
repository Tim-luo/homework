#!/usr/bin/env python
# -*- coding:utf-8 -*-

import select
import sys

while True:
    readable, writeable, error = select.select([sys.stdin,],[],[],1)
    '''select.select([sys.stdin,],[],[],1)用到I/O多路复用，第一个参数是列表，我放进去的是stdin就是我输入进去东西的描述符,
       相当于打开一个文件，和obj = socket()，类似的文件描述符，
       sys.stdin 他只是一个特殊的文件描述符= 终端的输入，一旦你输入OK select I/O多路复用他就感知到了。
       先看readable这个参数，其他的县不用看一旦你发生了我就他他发到readable里了，
       这里添加的就是修改的那个文件描述符，如果你一直没有修改过，那么readable他就是一个空的列表
    '''
    if sys.stdin in readable:
        print 'select get stdin',sys.stdin.readline()

'''
when runing the program get error :
Traceback (most recent call last):
  File "E:/study/GitHub/homework/tianshuai/share_3_select_socket.py", line 8, in <module>
    readable, writeable, error = select.select([sys.stdin,],[],[],1)
select.error: (10093, 'Either the application has not called WSAStartup, or WSAStartup failed')

when windows only use select socket !!!!!
'''