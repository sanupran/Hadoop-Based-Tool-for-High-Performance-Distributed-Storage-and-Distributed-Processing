#!/usr/bin/python

import commands

commands.getstatusoutput("export JAVA_HOME=/usr/java/jdk1.7.0_79")
commands.getstatusoutput("export PATH=$JAVA_HOME/bin:$PATH")
commands.getstatusoutput("export HADOOP_HOME=/hadoop2")
commands.getstatusoutput("export PATH=$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH")
