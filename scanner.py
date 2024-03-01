#!/bin/python3

import sys
import socket
from datetime import datetime

#Define our terget
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else: 
	print("Invalid amount of arguments.")
	print ("syntax: python3 scanner.py <ip>")

#Add a pretty banner
print("-" * 50)
print("scanning target: " +target)
print ("Time started: " +str(datetime.now()))
print("-" * 50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print(f"port {port} is open")
			s.close()

except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
except socket.gaierror:
	print ("Hostname could not be resolved")
except socket.error:
	print("could not connect to server.")
	sys.exit()
	 








