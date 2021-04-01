from cd import CreateDir as CD

if input("Клиент, загружен. Если у вас закрывается данное приложение когда вы нажимаете на \"Enter\", то напишите \"1\", если нет просто нажмите на \"Enter\"\nВыбор: -") == '1':CD()


import IPV4Read as ipv4

import socket, threading, time, os

key = 8194

shutdown = False
join = False

def receving (name, sock):
	while not shutdown:
		try:
			while True:
				data, addr = sock.recvfrom(1024)
				#print(data.decode("utf-8"))

				# Begin
				decrypt = ""; k = False
				for i in data.decode("utf-8"):
					if i == ":":
						k = True
						decrypt += i
					elif k == False or i == " ":
						decrypt += i
					else:
						decrypt += chr(ord(i)^key)
				print(decrypt)
				
				# End

				time.sleep(0.2)
		except:
			pass
host = ipv4.get_host() #("192.168.1.8")#socket.gethostbyname(socket.gethostname())
server_port = ipv4.get_port()
port = 0

server_host = ipv4.get_host_server()
server = (server_host,server_port)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

alias = input("Выберите своё имя: ")

rT = threading.Thread(target = receving, args = ("RecvThread",s))
rT.start()

while shutdown == False:
	if join == False:
		s.sendto(("["+alias + "] => присоединился ").encode("utf-8"),server)
		join = True
	else:
		try:
			message = input("\n\n")

			# Begin
			crypt = ""
			for i in message:
				crypt += chr(ord(i)^key)
			message = crypt
			# End

			if message != "":
				s.sendto(("["+alias + "] :: "+message).encode("utf-8"),server)
				
				s.sendto((message).encode("utf-8"),server)
			time.sleep(0.2)
		
		except:
			s.sendto(("["+alias + "] <= отключился ").encode("utf-8"),server)
			shutdown = True

rT.join()
s.close()
