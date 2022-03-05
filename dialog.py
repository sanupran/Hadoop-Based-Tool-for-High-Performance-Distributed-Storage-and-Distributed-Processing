#!/usr/bin/python

import start
import commands
import os
import hdfs
import operation
import mapreduce

def ip():
	b=commands.getstatusoutput("nmap -sn 192.168.43.10-110 -n |grep 'Nmap scan'| cut -d' ' -f5")
#os.system("dialog --textbox file.txt 10 30")


	c=b[1].split("\n")
	nn=c[0]
	jt=c[1]
	del c[0]
	del c[0]
	new1(nn,c,jt)
def value():
	d=open('/root/Desktop/choise.txt')
	choise=d.read()
	d.close()
	return choise
	
def dialog():
	os.system("dialog --menu 'select your choise' 20 40 4 1 'activate hdfs ' 2 'activate map-reduce ' 3 'operation' 4 'exit'  2>/root/Desktop/choise.txt")
	choise=value()
	return choise



def new1(nn,c,jt):
	choise=dialog()
	if choise == '1':
		start.nn(nn)
		print nn
		print jt
		for j in range(len(c)):
 			start.dn(c[j])
			print c[j]
		os.system("dialog --menu 'hdfs is successfully activated' 20 40 3 1 'hdfs operations ' 2 ' back' 3 'exit'  2>/root/Desktop/choise.txt")
		val=value()
		if val=='1':
			hdfs.hdfs()
		elif val == '2':
			new1(nn,c,jt)
		elif val == '3':
			exit()
	elif choise == '2':
		start.jt(jt)
		for l in range(len(c)):
 			start.tt(c[l])
		os.system("dialog --menu 'map-reduce is successfully activated' 20 40 3 1 'map-reduce operations ' 2 ' back' 3 'exit'  2>/root/Desktop/choise.txt")
		val=value()
		if val=='1':
			os.system("dialog --infobox ' welcome to map-reduce '  10 30 ")
			mapreduce.mapreduce()
		elif val == '2':
			new1(nn,c,jt)
		elif val == '3':
			exit()
	elif choise == '3':
		operation.operation()
	elif choise == '4':
		exit()
