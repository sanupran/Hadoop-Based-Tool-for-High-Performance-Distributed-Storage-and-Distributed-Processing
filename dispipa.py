#!/usr/bin/python


import commands
import os

def dispipa():
	commands.getstatusoutput("python ippre.py >file.txt")
	commands.getstatusoutput("nmap -sn 192.168.43.10-110 -n |grep 'Nmap scan'| cut -d' ' -f5 >>file.txt")
	os.system("dialog --textbox file.txt 20 60")
