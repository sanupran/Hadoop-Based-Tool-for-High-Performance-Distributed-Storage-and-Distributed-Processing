#!/usr/bin/python
import commands
import os


#hadoop 1 installation
def hadoop_1install(ip):
     print "coppying hadoop software to client"
     commands.getstatusoutput("scp hadoop-1.2.1-1.x86_64.rpm root@{}:".format(ip))
     print "installing hadoop on client system"
     commands.getstatusoutput("ssh {} rpm -ivh hadoop-1.2.1-1.x86_64.rpm --replacefiles".format(ip))
          
     
     #p=commands.getstatusoutput("ssh {} hadoop -version".format(ip))
     #print p[1]
     #ad=commands.getstatusoutput("ssh 192.168.43.51 /usr/java/jdk1.7.0_79/bin/jps")
     #print ad[1]



#jdk installation
def jdk_install(ip):
    os.system("dialog --infobox 'coppying jdk software to client '  10 30 ")
#    print "coppying jdk software to client"
    commands.getstatusoutput("scp jdk-7u79-linux-x64.rpm root@{}:".format(ip))
    os.system("dialog --infobox 'installing jdk on client system '  10 30 ")
#    print "installing jdk on client system"
    commands.getstatusoutput("ssh {} yum install jdk-7u79-linux-x64.rpm -y".format(ip))
    
#    print "seating path for hadoop"
#    commands.getstatusoutput("ssh 192.168.43.{} export JAVA_HOME=/usr/java/#jdk1.7.0_79".format(ip))
#    commands.getstatusoutput("ssh 192.168.43.{} export PATH=$JAVA_HOME/bin:$PATH".format(ip))


#hadoop 2 installation
def hadoop_2install(ip):
#     print "hello"
     os.system("dialog --infobox 'coppying and installing hadoop software to client '  10 30 ")
#     print "coppying hadoop software to client"  
#     commands.getstatusoutput("scp -r hadoop-2.6.4 root@{}:".format(ip))
#     print "hiiiii"
#     commands.getstatusoutput("scp -r hadoop2 root@{}:/".format(ip))
     os.system("scp hadoop-2.6.4.tar.gz root@{}:".format(ip))
     os.system("ssh {} tar -xvzf hadoop-2.6.4.tar.gz".format(ip))
     os.system("ssh {} mv hadoop-2.6.4 /hadoop2".format(ip))
#    os.system("scp -r hadoop2 root@{}:/".format(ip))
     commands.getstatusoutput("scp  .bashrc root@{}:/root/".format(ip))
     commands.getstatusoutput("scp -r startbash.py root@{}:".format(ip))
     commands.getstatusoutput("ssh {} python startbash.py".format(ip))
#     print "biiiiiii"
#     print "extracting hadoop"
#     commands.getstatusoutput("ssh {} tar -xvzf hadoop-2.6.4.tar.gz".format(ip))
#     commands.getstatusoutput("scp hadoop-2.6.4 root@192.168.43.{}:".format(ip))
#     print "seating path for hadoop"
#     commands.getstatusoutput("ssh 192.168.43.{} mkdir /hadoop2".format(ip))
#     commands.getstatusoutput("ssh {} mv hadoop-2.6.4 /hadoop2".format(ip))
#     commands.getstatusoutput("ssh 192.168.43.{} export HADOOP_HOME=/hadoop2".format(ip))
#     commands.getstatusoutput("ssh 192.168.43.{} export PATH=$HADOOP/bin:$HADOOP_HOME/sbin:$PATH".format(ip))
