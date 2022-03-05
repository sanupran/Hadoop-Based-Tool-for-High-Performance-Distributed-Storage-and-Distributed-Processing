#!/usr/bin/python

import os
import getpass
import commands
import time
import install

os.system("tput setaf 1")
print "\t\t\tWelcome to hadoop data distribution environment"


os.system("tput setaf 0")
user_name=raw_input("please enter username  ")
passwd=getpass.getpass("enter your password  ")


  
if passwd=="redhat":
    print "welcom to redhat"
else :
    print "you are not correct user"
    raw_input()
    exit()


if passwd=="redhat":
    print "press 1 to configure hdfs automatically"
    print "press 2 to configure hdfs automatically"

y=raw_input("enter your choise ")

if int(y)==1 :
    print "press 1 to configure hadoop version 1"
    print "press 2 to configure hadoop version 2"
    print "press 3 to exit"


    choise=raw_input("enter your input ")


    if int(choise)==1:
        install.hadoop_1install(45)
    elif int(choise)==2:
        install.hadoop_2install(45)
    elif int(choise)==3:
        exit()
    else:
        print "invalid input"
else :
    print "invalid input"






print "press enter to exit"
raw_input()
