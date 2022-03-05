#!/usr/bin/python


import commands
import os
def client():
	b=commands.getstatusoutput("rpm -q jdk")
    	d=b[1]
    	i=d[0:3]
#    print i
    	if i == "jdk":
		os.system("dialog --infobox ' jdk is already installed in your system '  10 30 ")
#        print "jdk is already installed in your system"
    	else:
#	commands.getstatusoutput("jdk-7u79-linux-x64.rpm root@{}:")
#    print "installing jdk on client system"
		os.system("dialog --infobox ' installing jdk in your system '  10 30 ")
        	commands.getstatusoutput("yum install jdk-7u79-linux-x64.rpm -y")
            
            
    	c=commands.getstatusoutput("hadoop version | grep 'Hadoop'")
    	h=c[1]
    	g=h[0:6]
	f=0
    	if g=='Hadoop':
		os.system("dialog --infobox ' hadoop is already installed in your system '  10 30 ")
#		print "hadoop is already installed in your system"
		f=1
    	else:
		os.system("dialog --infobox 'we are configuring hadoop in your system'  10 30 ")
		commands.getstatusoutput("cp -rvf hadoop2 /")
        	commands.getstatusoutput("yes | cp -rvf .bashrc /root/")
		commands.getstatusoutput("chmod 777 -R /hadoop2")
#		commands.getstatusoutput("setpath.py root@{}:")
#		commands.getstatusoutput("python setpath.py")
	if f==1:
		os.system("dialog --infobox ' this system is configured as client '  10 30 ")
		commands.getstatusoutput("hostnamectl set-hostname")
		commands.getstatusoutput("yes | cp hadoop2_conf/client/core-site.xml /hadoop2/etc/hadoop/")
		commands.getstatusoutput("yes | cp hadoop2_conf/client/yarn-site.xml /hadoop2/etc/hadoop/")
		commands.getstatusoutput("yes | cp hadoop2_conf/client/mapred-site.xml /hadoop2/etc/hadoop/")
		commands.getstatusoutput("yes | cp hosts /etc/")
	os.system("source /root/.bashrc")
