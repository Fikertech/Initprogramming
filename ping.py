import os
import subprocess
import platform

host = input("Enter target: ")

def ping(host):
	param = '-n' if platform.system().lower() == 'windows' else '-c'
	command = ['ping', param, '1000', host]
	return subprocess.call(command)

print(ping(host))	
