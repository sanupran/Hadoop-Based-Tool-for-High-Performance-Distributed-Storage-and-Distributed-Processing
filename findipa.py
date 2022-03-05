#!/usr/bin/python


import commands
import check
import start
import os
import dispipa
import client
import dialog
import stop

def findipa():
	dispipa.dispipa()
	b=commands.getstatusoutput("nmap -sn 192.168.43.10-110 -n |grep 'Nmap scan'| cut -d' ' -f5")
#os.system("dialog --textbox file.txt 10 30")

	q=0
	c=b[1].split("\n")
	for m in range(len(c)):
		stop.stop(c[m])
	nn=c[0]
#print "select one which you wanted as namenode "
#print "options"+"       "+"IP"+"         "+"RAM"
#ram=[]
#for i in range(len(c)):
#	ram[i]=commands.getstatusoutput("ssh {} cat /proc/meminfo |grep 'MemTotal'|cut -d' ' -#f9".format(c[i])
#print "the available systems are "
#for j in range(len(c)):
#	print c[j]

#print "system having ip "+c[0]+"is configured as namenode"
	os.system("dialog --infobox ' system having ip {} is configured as namenode '  10 30 ".format(c[0]))

	r=check.check("{}".format(c[0]),2)
	if r == 1:
		commands.getstatusoutput("ssh {} hostnamectl set-hostname nn".format(c[0]))
		commands.getstatusoutput("scp hadoop2_conf/nn/core-site.xml root@{}:/hadoop2/etc/hadoop/".format(c[0]))
		commands.getstatusoutput("scp hadoop2_conf/nn/hdfs-site.xml root@{}:/hadoop2/etc/hadoop/".format(c[0]))
		commands.getstatusoutput("scp hosts root@{}:/etc/".format(c[0]))
		q=1
		commands.getstatusoutput("ssh {} reboot".format(c[0]))
		#commands.getstatusoutput("ssh {} hdfs namenode -format".format(c[0]))
		nn=c[0]
	#exit()
	


#print "system having ip "+c[1]+"is configured as job-Tracker"
	os.system("dialog --infobox ' system having ip {} is configured as job-Tracker '  10 30 ".format(c[1]))
	rjk=check.check("{}".format(c[1]),2)
	if rjk==1:
		commands.getstatusoutput("ssh {} hostnamectl set-hostname jt".format(c[1]))
		commands.getstatusoutput("scp hadoop2_conf/jt/core-site.xml root@{}:/hadoop2/etc/hadoop/".format(c[1]))
		commands.getstatusoutput("scp hadoop2_conf/jt/yarn-site.xml root@{}:/hadoop2/etc/hadoop/".format(c[1]))
		commands.getstatusoutput("scp hosts root@{}:/etc/".format(c[1]))
		commands.getstatusoutput("ssh {} reboot".format(c[1]))
		jt=c[1]



#print "system having ip "+c[2]+"is configured as job-Tracker"
	os.system("dialog --infobox 'your system is configured as client '  10 30 ")
	client.client()

#rc=check.check("{}".format(c[2]),2)
#if rc==1:
#	commands.getstatusoutput("ssh {} hostnamectl set-hostname".format(c[2]))
#	commands.getstatusoutput("scp hadoop2_conf/client/core-site.xml root@{}:/hadoop2/etc/hadoop/".format(c[2]))
#	commands.getstatusoutput("scp hadoop2_conf/client/yarn-site.xml root@{}:/hadoop2/etc/hadoop/".format(c[2]))
#	commands.getstatusoutput("scp hadoop2_conf/client/mapred-site.xml root@{}:/hadoop2/etc/hadoop/".format(c[2]))
#	commands.getstatusoutput("scp hosts root@{}:/etc/".format(c[2]))
#	commands.getstatusoutput("ssh {} source /root/.bashrc".format(c[2]))
#	client=c[2]



#del c[0]
	del c[0]
	del c[0]
	for k in range(len(c)):
#	print "system having ip "+c[k]+"is configured as datanode"
		rdn=check.check("{}".format(c[k]),2)
		if rdn==1:
			os.system("dialog --infobox ' system having ip {} is configured as datanode '  10 30 ".format(c[k]))
			commands.getstatusoutput("ssh {0} hostnamectl set-hostname dn{1}".format(c[k],k+1))
			commands.getstatusoutput("scp hadoop2_conf/dn/core-site.xml root@{}:/hadoop2/etc/hadoop/".format(c[k]))
			commands.getstatusoutput("scp hadoop2_conf/dn/hdfs-site.xml root@{}:/hadoop2/etc/hadoop/".format(c[k]))
			commands.getstatusoutput("scp hadoop2_conf/dn/yarn-site.xml root@{}:/hadoop2/etc/hadoop/".format(c[k]))
			commands.getstatusoutput("scp hosts root@{}:/etc/".format(c[k]))
			commands.getstatusoutput("ssh {} reboot".format(c[k]))
	#r=check.check("{}".format(nn),2)
	if q == 0:
		print "no need to format"
	else :
		commands.getstatusoutput("ssh {} hdfs namenode -format -Y".format(nn))
	dialog.ip()
	
