#!/usr/bin/python


import commands
import os

def file():
	f1=open('/root/Desktop/choise.txt')
	file_name=f1.read()
	f1.close()
	return file_name

def dispip():
	commands.getstatusoutput("python ippre.py >file.txt")
	commands.getstatusoutput("nmap -sn 192.168.43.10-110 -n |grep 'Nmap scan'| cut -d' ' -f5 >>file.txt")
	

	b=commands.getstatusoutput("nmap -sn 192.168.43.10-110 -n |grep 'Nmap scan'| cut -d' ' -f5")
#os.system("dialog --textbox file.txt 10 30")


	c=b[1].split("\n")
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
	print "nn "+nn
	print "jt "+jt
	print dg
	"""os.system("dialog --menu 'select namenode' 20 40 {0} ".format(g)+d+" 2>/root/Desktop/choise.txt")
	os.system("dialog --menu 'select your choise' 20 40 2 1 ' hadoop install automatically' 2 ' hadoop install manually ' 3 ' exit '  2>/root/Desktop/choise.txt")
	os.system("dialog --inputbox '{}' 10 30  2>/root/Desktop/usr.txt")	
	os.system("dialog --textbox file.txt 20 60")"""
