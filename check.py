#!/usr/bin/python

import commands
import install




def dialog():
   c=commands.getstatusoutput("rpm -q dialog | grep 'dialog'")
   h=c[1]
   g=h[0:6]
#    print g
   if g=="dialog":
	print "dialog is already installed in your system"
	return 0
   else:
#        print "no hadoop is found in your system"
#        x=raw_input("\n\npress enter to install\npress space to exit")
#	if version==1 :
#                	install.hadoop_1install(ip)
#        else: 
#			if x==" ":
#				exit()
        c=commands.getstatusoutput("yum install dialog-1.2-4.20130523.el7.i686.rpm")
#	commands.getstatusoutput("scp setpath.py root@{}:".format(ip))
#	commands.getstatusoutput("ssh {} python setpath.py".format(ip))
	return 1 

def nmap():
    c=commands.getstatusoutput("rpm -q nmap | grep 'nmap'")
    h=c[1]
    g=h[0:4]
#    print g
    if g=="nmap":
	print "nmap is already installed in your system"
	return 0
    else:
        c=commands.getstatusoutput("yum install nmap-6.40-7.el7.x86_64.rpm")
	return 1 

def check(ip,version):
    b=commands.getstatusoutput("ssh {} rpm -q jdk".format(ip))
    d=b[1]
    i=d[0:3]
#    print i
    if i == "jdk":
        print "jdk is already installed in your system"
    else:
#        print "no jdk found in your system"
#        y=raw_input("\n\npress enter to install \n press space to exit")
#        if y == " ": 
#        	raw_input()
#        else :
	install.jdk_install(ip)
            
            
    c=commands.getstatusoutput("ssh {} hadoop version | grep 'Hadoop'".format(ip))
    h=c[1]
    g=h[0:6]
#    print g
    if g=="Hadoop":
	print "hadoop is already installed in your system"
	return 0
    else:
#        print "no hadoop is found in your system"
#        x=raw_input("\n\npress enter to install\npress space to exit")
#	if version==1 :
#                	install.hadoop_1install(ip)
#        else: 
#			if x==" ":
#				exit()
        install.hadoop_2install(ip)
#	commands.getstatusoutput("scp setpath.py root@{}:".format(ip))
#	commands.getstatusoutput("ssh {} python setpath.py".format(ip))
	return 1
    
    
        
