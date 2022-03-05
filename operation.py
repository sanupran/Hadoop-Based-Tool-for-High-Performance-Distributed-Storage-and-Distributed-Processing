#!/usr/bin/python

import dialog
import os
import hdfs
import mapreduce

def operation():
	os.system("dialog --menu 'operations' 20 40 4 1 'hdfs operations ' 2 'map-reduce operation' 3 'back' 4 'exit'  2>/root/Desktop/choise.txt")
	v=dialog.value()
	if v=='1':
		hdfs.hdfs()
	elif v == '2':
		mapreduce.mapreduce()
	elif v == '3':
		dialog.ip()
	elif v == '4':
		exit()
