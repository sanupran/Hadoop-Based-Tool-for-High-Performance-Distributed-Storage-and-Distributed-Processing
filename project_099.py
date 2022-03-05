#!/usr/bin/python

import commands
import os
import time
import findip
import findipa

os.system("dialog --infobox '\tWELCOME To \n\n\n\n\n\n\n\n\t High Performance \n Distributed computing and \nDistributed storage\n tool using Hadoop   '  20 60 ")
time.sleep(4)
os.system("dialog --inputbox 'enter username' 10 30  2>/root/Desktop/usr.txt")
time.sleep(1)
os.system("dialog --passwordbox 'enter password' 10 30 2>/root/Desktop/pass.txt" )
time.sleep(2)
f1=open('/root/Desktop/usr.txt')
usr=f1.read()
f1.close()

f2=open('/root/Desktop/pass.txt')
password=f2.read()
f2.close()

if usr=='hadoop' and password=='redhat':
    os.system('clean')
    os.system("dialog --infobox 'welcome to the world of BIG DATA  '  20 60 ")
    os.system("dialog --menu 'select your choise' 20 40 3 1 ' hadoop install automatically' 2 ' hadoop install manually ' 3 ' exit '  2>/root/Desktop/choise.txt")
else:
    os.system("dialog --infobox 'YOU ARE NOT A VALID USER  '  20 60 ")
    time.sleep(1)
    os.system("dialog --infobox 'THANK YOU FOR USING OUR SERVICE'  20 60 ") 
    
d=open('/root/Desktop/choise.txt')
choise=d.read()
d.close()

if choise == '1':
#    os.system("dialog --infobox 'WELCOME TO HADOOP 1 '  20 60 ")
    findipa.findipa()
elif choise == '2':
    findip.findip()    
elif choise == '3':
    exit()

