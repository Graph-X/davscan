##############################################################
#    sploits is part of the davscan project
#    the goal is to take server fingerprinting information
#    from a server and find public exploits for the server
#    the library relies on searchsploit on the local machine 
#    for this information. Basically use this on Kali
##############################################################

import subprocess
import re
	
class IIS5:
    def __init__(self, m=False, d=False):
	command = 'searchsploit'
	if m:
		command = command + ' --no-msf'
	command = command + ' -t IIS 5.0'
	if d:
		command = command + ' | grep -v "/dos/"'
        self.sploits = {'Server': 'IIS 5.0'}
        results = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        out = results.communicate()
        for line in out[0].splitlines():
                if "|" in line:
                    kv = line.split("|")
                    if ( kv[0].strip()  != '' or kv[0].strip() != 'Server' or kv[0].strip() != 'Exploit Title'):
                        self.sploits[kv[0].strip()] = kv[1].strip()
class IIS6:
    def __init__(self, m=False, d=False):
	command = 'searchsploit'
	if m:
		command = command + ' --no-msf'
	command = command + ' -t IIS 6.0'
	if d:
		command = command + ' | grep -v "/dos/"'
        self.sploits = {'Server': 'IIS 6.0'}
        results = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        out = results.communicate()
        for line in out[0].splitlines():
            if "|" in line:
                kv = line.split("|")
                if ( kv[0].strip()  != '' or kv[0].strip() != 'Server' or kv[0].strip() != 'Exploit Title'):
                    self.sploits[kv[0].strip()] = kv[1].strip()

class IIS75:
    def __init__(self, m=False, d=False):
	command = 'searchsploit'
	if m:
		command = command + ' --no-msf'
	command = command + ' -t IIS 7.5'
	if d:
		command = command + ' | grep -v "/dos/"'
        self.sploits = {'Server': 'IIS 7.5'}
        results = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        out = results.communicate()
        for line in out[0].splitlines():
            if "|" in line:
                kv = line.split("|")
                if ( kv[0].strip()  != '' or kv[0].strip() != 'Server' or kv[0].strip() != 'Exploit Title'):
                    self.sploits[kv[0].strip()] = kv[1].strip()

class Apache13:
    def __init__(self, m=False, d=False):
	command = 'searchsploit'
	if m:
		command = command + ' --no-msf'
	command = command + ' -t Apache 1.3'
	if d:
		command = command + ' | grep -v "/dos/"'
        self.sploits = {'Server': 'Apache 1.3'}
        results = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        out = results.communicate()
        for line in out[0].splitlines():
            if "|" in line:
                kv = line.split("|")
                if ( kv[0].strip()  != '' or kv[0].strip() != 'Server' or kv[0].strip() != 'Exploit Title'):
                        self.sploits[kv[0].strip()] = kv[1].strip()
class Apache20:
    def __init__(self, m=False, d=False):
	command = 'searchsploit'
	if m:
		command = command + ' --no-msf'
	command = command + ' -t Apache 2.0'
	if d:
		command = command + ' | grep -v "/dos/"'
        self.sploits = {'Server': 'Apache 2.0'}
        results = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        out = results.communicate()
        for line in out[0].splitlines():
            if "|" in line:
                kv = line.split("|")
                if ( kv[0].strip()  != '' or kv[0].strip() != 'Server' or kv[0].strip() != 'Exploit Title'):
                        self.sploits[kv[0].strip()] = kv[1].strip()
class Apache22:
    def __init__(self, m=False, d=False):
	command = 'searchsploit'
	if m:
		command = command + ' --no-msf'
	command = command + ' -t Apache 2.2'
	if d:
		command = command + ' | grep -v "/dos/"'
        self.sploits = {'Server': 'Apache 2.2'}
        results = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        out = results.communicate()
        for line in out[0].splitlines():
            if "|" in line:
                kv = line.split("|")
                if ( kv[0].strip()  != '' or kv[0].strip() != 'Server' or kv[0].strip() != 'Exploit Title'):
                    self.sploits[kv[0].strip()] = kv[1].strip()
class Apache24:
    def __init__(self, m=False, d=False):
	command = 'searchsploit'
	if m:
		command = command + ' --no-msf'
	command = command + ' -t Apache 2.4'
	if d:
		command = command + ' | grep -v "/dos/"'
        self.sploits = {'Server': 'Apache 2.4'}
        results = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        out = results.communicate()
        for line in out[0].splitlines():
            if "|" in line:
                kv = line.split("|")
                if ( kv[0].strip()  != '' or kv[0].strip() != 'Server' or kv[0].strip() != 'Exploit Title'):
                    self.sploits[kv[0].strip()] = kv[1].strip()
class nginx06:
    def __init__(self, m=False, d=False):
	command = 'searchsploit'
	if m:
		command = command + ' --no-msf'
	command = command + ' -t nginx 0.6'
	if d:
		command = command + ' | grep -v "/dos/"'
        self.sploits = {'Server': 'nginx 0.6'}
        results = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        out = results.communicate()
        for line in out[0].splitlines():
            if "|" in line:
                kv = line.split("|")
                if ( kv[0].strip()  != '' or kv[0].strip() != 'Server' or kv[0].strip() != 'Exploit Title'):
                    self.sploits[kv[0].strip()] = kv[1].strip()
class nginx078:
    def __init__(self, m=False, d=False):
	command = 'searchsploit'
	if m:
		command = command + ' --no-msf'
	command = command + ' -t nginx 0.7'
	if d:
		command = command + ' | grep -v "/dos/"'
        self.sploits = {'Server': 'nginx 0.7 or nginx 0.8'}
        results = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        out = results.communicate()
        for line in out[0].splitlines():
            if "|" in line:
                kv = line.split("|")
                if ( kv[0].strip()  != '' or kv[0].strip() != 'Server' or kv[0].strip() != 'Exploit Title'):
                    self.sploits[kv[0].strip()] = kv[1].strip()
class nginx11:
    def __init__(self, m=False, d=False):
	command = 'searchsploit'
	if m:
		command = command + ' --no-msf'
	command = command + ' -t nginx 1.1.7'
	if d:
		command = command + ' | grep -v "/dos/"'
        self.sploits = {'Server': 'nginx 1.1.7'}
        results = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        out = results.communicate()
        for line in out[0].splitlines():
            if "|" in line:
                kv = line.split("|")
                if ( kv[0].strip()  != '' or kv[0].strip() != 'Server' or kv[0].strip() != 'Exploit Title'):
                    self.sploits[kv[0].strip()] = kv[1].strip()
class nginx134:
    def __init__(self, m=False, d=False):
	command = 'searchsploit'
	if m:
		command = command + ' --no-msf'
	command = command + ' -t nginx 1.3.4'
	if d:
		command = command + ' | grep -v "/dos/"'
        self.sploits = {'Server': 'nginx 1.3.4'}
        results = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        out = results.communicate()
        for line in out[0].splitlines():
            if "|" in line:
                kv = line.split("|")
            if ( kv[0].strip()  != '' or kv[0].strip() != 'Server' or kv[0].strip() != 'Exploit Title'):
                self.sploits[kv[0].strip()] = kv[1].strip()
class PHP:
    def __init__(self, v, m=False, d=False):
	p = 'PHP ' + v
	command = 'searchsploit'
	if m:
		command = command + ' --no-msf'
	command = command + ' -e' + p
	if d:
		command = command + ' | grep -v "/dos/"'
	self.sploits = {}
	results = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
	out = results.communicate()
	for line in out[0].splitlines():
		if "|" in line:
			kv = line.split("|")
		if ( kv[0].strip()  != '' or kv[0].strip() != 'Server' or kv[0].strip() != 'Exploit Title'):
			self.sploits[kv[0].strip()] = kv[1].strip()
class ASP:
    def __init__(self, v, m=False, d=False):
        a = 'ASP.NET ' + v
	command = 'searchsploit'
	if m:
		command = command + ' --no-msf'
	command = command + '-e ' + a
	if d:
		command = command + ' | grep -v "/dos/"'
	self.sploits = {}
	results = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
	out = results.communicate()
	for line in out[0].splitlines():
		if "|" in line:
			kv = line.split("|")
		if ( kv[0].strip()  != '' or kv[0].strip() != 'Server' or kv[0].strip() != 'Exploit Title'):
			self.sploits[kv[0].strip()] = kv[1].strip()

