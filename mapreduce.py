#!/usr/bin/python

import dialog
import os
import operation
import commands

def file():
	f1=open('/root/Desktop/file.txt')
	file_name=f1.read()
	f1.close()
	return file_name

#def fileread():
#	f1=open('/root/Desktop/fileread.txt')
#	file_name=f1.read()
#	f1.close()
	return file_name
def mapreduce():
	os.system("dialog --menu 'select your choise' 20 40 3 1 'worldcount ' 2 'back' 3 'exit'  2>/root/Desktop/choise.txt")
	v=dialog.value()
	if v == '1':
		os.system("dialog --inputbox 'enter file name to do wordcount' 10 30  2>/root/Desktop/file.txt")
		name=file()
		os.system("dialog --infobox 'performing wordcount on {} file '  20 60 ".format(name))
#		time.sleep(2)
		commands.getstatusoutput("yarn jar /hadoop2/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.6.4.jar wordcount /{} /output6".format(name))
#		os.system(" hdfs dfs -cat /output6/part-r-00000")
		commands.getstatusoutput("python g1.py >file.txt")
		commands.getstatusoutput("hdfs dfs -cat /output6/part-r-00000 >>file.txt")
		os.system("dialog --textbox file.txt 20 60")
		mapreduce()
	elif v == '2':
		operation.operation()
	elif v == '3':
		exit()	
