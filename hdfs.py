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
def hdfs():
	os.system("dialog --menu 'select your choise' 20 40 5 1 'upload file ' 2 'remove file ' 3 'read file' 4 'back' 5 'exit'  2>/root/Desktop/choise.txt")
	v=dialog.value()
	if v == '1':
		os.system("dialog --inputbox 'enter file name to be uploaded' 10 30  2>/root/Desktop/file.txt")
		name=file()
		print name
		os.system("dialog --infobox 'uploading {} file to hdfs '  20 60 ".format(name))
#		time.sleep(2)
		commands.getstatusoutput("hdfs dfs -put {} /".format(name))
		hdfs()
	elif v == '2':
		os.system("dialog --inputbox 'enter file name to be removed' 10 30  2>/root/Desktop/file.txt")
		os.system("dialog --infobox 'removing {} file from hdfs '  20 60 ".format(name))
#		time.sleep(1)
		hdfs()
	elif v == '3':
		os.system("dialog --inputbox 'enter file name to be read' 10 30  2>/root/Desktop/file.txt")
#		time.sleep(1)
		name=file()
		os.system("hdfs dfs -cat /{}".format(name))
#		y=open('/root/Desktop/fileread.txt', mode='a')
#		y.write(v[1])
#		y.close()
#		os.system("dialog --textbox fileread.txt 10 30")
		hdfs()
	elif v == '4':
		operation.operation()
	elif v == '5':
		exit()	
