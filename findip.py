#!/usr/bin/python


import commands
import check
import start
import os
import dispip
import client
import dialog1
import stop

def file():
	f1=open('/root/Desktop/choise.txt')
	file_name=f1.read()
	f1.close()
	return file_name

def findip():
	#dispip.dispip()
	commands.getstatusoutput("python ippre.py >file.txt")
	commands.getstatusoutput("nmap -sn 192.168.43.10-110 -n |grep 'Nmap scan'| cut -d' ' -f5 >>file.txt")
	

	b=commands.getstatusoutput("nmap -sn 192.168.43.10-110 -n |grep 'Nmap scan'| cut -d' ' -f5")
#os.system("dialog --textbox file.txt 10 30")

	q=0
	c=b[1].split("\n")
	for m in range(len(c)):
		stop.stop(c[m])
	dg=c
	g=len(c)
	d=""
	for i in range(len(c)):
		e="{0} '{1}' ".format(i+1,c[i])
		d=d+"\n"+e
	os.system("dialog --inputbox 'select namenode {}' 10 30  2>/root/Desktop/choise.txt".format(d))
	no=int(file())
	nn=c[no-1]
	fg=c
	fg.remove(nn)
	d=""
	for i in range(len(fg)):
		e="{0} '{1}' ".format(i+1,fg[i])
		d=d+"\n"+e
	os.system("dialog --inputbox 'select job-tracker {}' 10 30  2>/root/Desktop/choise.txt".format(d))
	n=int(file())
	jt=fg[n-1]
	dg.remove(jt)
	os.system("dialog --infobox ' system having ip {} is configured as namenode '  10 30 ".format(nn))
	host="127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4\n::1         localhost localhost.localdomain localhost6 localhost6.localdomain6"
	host=host+"\n{}   nn".format(nn)+"\n{}   jt".format(jt)+"\n192.168.43.5  client"
	for i in range(len(dg)):
		host=host+"\n{0} dn{1}".format(dg[i],i+1)
	fil=open('host/hosts','w')
	fil.write(host)
	fil.close()
	r=check.check("{}".format(nn),2)
	if r == 1:
		commands.getstatusoutput("ssh {} hostnamectl set-hostname nn".format(nn))
		commands.getstatusoutput("scp hadoop2_conf/nn/core-site.xml root@{}:/hadoop2/etc/hadoop/".format(nn))
		commands.getstatusoutput("scp hadoop2_conf/nn/hdfs-site.xml root@{}:/hadoop2/etc/hadoop/".format(nn))
		commands.getstatusoutput("scp host/hosts root@{}:/etc/".format(nn))
		commands.getstatusoutput("ssh {} source /root/.bashrc".format(nn))
		q=1
		commands.getstatusoutput("ssh {} source reboot".format(nn))
		#commands.getstatusoutput("ssh {} hdfs namenode -format".format(nn))
		#nn=c[0]
	#exit()
	


#print "system having ip "+c[1]+"is configured as job-Tracker"
	os.system("dialog --infobox ' system having ip {} is configured as job-Tracker '  10 30 ".format(jt))
	rjk=check.check("{}".format(jt),2)
	if rjk==1:
		commands.getstatusoutput("ssh {} hostnamectl set-hostname jt".format(jt))
		commands.getstatusoutput("scp hadoop2_conf/jt/core-site.xml root@{}:/hadoop2/etc/	hadoop/".format(jt))
		commands.getstatusoutput("scp hadoop2_conf/jt/yarn-site.xml root@{}:/hadoop2/etc/hadoop/".format(jt))
		commands.getstatusoutput("scp host/hosts root@{}:/etc/".format(jt))
		commands.getstatusoutput("ssh {} reboot".format(jt))
		#commands.getstatusoutput("ssh {} source /root/.bashrc".format(jt))
		#jt=c[1]



#print "system having ip "+c[2]+"is configured as job-Tracker"
	os.system("dialog --infobox 'your system is configured as client '  10 30 ")
	client.client()
	





#del c[0]
	for k in range(len(dg)):
#	print "system having ip "+c[k]+"is configured as datanode"
		rdn=check.check("{}".format(dg[k]),2)
		if rdn==1:
			os.system("dialog --infobox ' system having ip {} is configured as datanode '  10 30 ".format(dg[k]))
			commands.getstatusoutput("ssh {0} hostnamectl set-hostname dn{1}".format(dg[k],k+1))
			commands.getstatusoutput("scp hadoop2_conf/dn/core-site.xml root@{}:/hadoop2/etc/hadoop/".format(dg[k]))
			commands.getstatusoutput("scp hadoop2_conf/dn/hdfs-site.xml root@{}:/hadoop2/etc/hadoop/".format(dg[k]))
			commands.getstatusoutput("scp hadoop2_conf/dn/yarn-site.xml root@{}:/hadoop2/etc/hadoop/".format(dg[k]))
			commands.getstatusoutput("scp host/hosts root@{}:/etc/".format(dg[k]))
			commands.getstatusoutput("ssh {} reboot".format(dg[k]))
	
	
	for m in range(len(c)):
		commands.getstatusoutput("scp host/hosts root@{}:/etc/".format(c[m]))
	commands.getstatusoutput("yes | cp host/hosts /etc/")
	#r=check.check("{}".format(nn),2)
	if q == 0:
		print "no need to format"
	else :
		commands.getstatusoutput("ssh {} hdfs namenode -format -Y".format(nn))
	dialog1.ip(nn,jt,dg)
