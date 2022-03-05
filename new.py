#!/usr/bin/python
import commands 
 
b=commands.getstatusoutput("nmap -sn 192.168.43.0-255 -n | grep '192' ")

print b[1]

f=open("b.txt","w+")
f.write(b[1])
f.close()


