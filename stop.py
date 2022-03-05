#!/usr/bin/python

import commands

def stop(ip):
	commands.getstatusoutput("ssh {} source /root/.bashrc".format(ip))
	commands.getstatusoutput("ssh {} systemctl stop firewalld".format(ip))
	commands.getstatusoutput("ssh {} setenforce 0".format(ip))
