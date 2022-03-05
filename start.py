#!/usr/bin/python

import commands

def nn(ip):
	#commands.getstatusoutput("ssh {} hdfs namenode -format".format(ip))
	commands.getstatusoutput("ssh {} hadoop-daemon.sh start namenode".format(ip))

def jt(ip):
	commands.getstatusoutput("ssh {} yarn-daemon.sh start resourcemanager".format(ip))

def dn(ip):
	commands.getstatusoutput("ssh {} hadoop-daemon.sh start datanode".format(ip))

def tt(ip):
	commands.getstatusoutput("ssh {} yarn-daemon.sh start nodemanager".format(ip))
