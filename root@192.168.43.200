#!/usr/bin/python

import commands
import socket

x=raw_input("enter your data ")
#def client_req(x):
    s=socket.socket(socket.AF_INET,SOCK_DGRAM,0)
    
    ip="192.168.43.200"
    port=1234

    s.bind(ip,port)
    s.sendto(x,("",1234))
