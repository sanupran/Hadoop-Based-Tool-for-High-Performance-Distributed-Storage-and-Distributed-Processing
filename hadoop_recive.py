#!/usr/bin/python

import commands
import socket

#x=raw_input("enter your data ")
#def client_req(x):
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
#s=socket.socket()
    
ip="192.168.43.200"
port=1234


s.bind((ip,port))
x=s.recv(10)
print "the output is "+x+" data"
