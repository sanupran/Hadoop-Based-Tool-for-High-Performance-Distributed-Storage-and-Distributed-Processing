#!/usr/bin/python

#import check
import commands
#check.check("192.168.43.16",2)

c=commands.getstatusoutput("ssh 192.168.43.16 hadoop version | grep 'Hadoop'")
h=c[1]
g=h[0:6]
print g
if g=="Hadoop":
	print "hadoop is already installed in your system"
else:
        print "no hadoop is found in your system"
        x=raw_input("press 1 to install")
