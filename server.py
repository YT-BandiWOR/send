import IPV4Read as ipv4
import socket, time

from cd import CreateDir as CD
if input("Сервер, загружен. Если у вас закрывается данное приложение когда вы нажимаете на \"Enter\", то напишите \"1\", если нет просто нажмите на \"Enter\"\nВыбор: -") == '1':
	CD()


host = ipv4.get_host()#"192.168.1.8"#socket.gethostbyname(socket.gethostname())
port = ipv4.get_port()#9090

clients = []

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host , port))

quit = False
print("[!] Сервер запущен")
print(f"\nНастроки сервера:\nХост: {host}\nПорт: {port}\n")



i_r = 1 
while not quit:
	try:
		data, addr = s.recvfrom(1024)
		
		print("\n\nПакет данных №"+str(i_r))
		print("--------------------------------\n\n")
		print("[!] Данные: ", data, "\nADDR: ", addr)

		print("Последние данные с сервера",s.recvfrom(1024))
		print('[!] Данные, которые пришли от "SERVER":')
		print("**********************")
		print("Список клиентов: \n",
			  "-----------------\n",
			  "№        данные \n ")
		for i in range(len(clients)):
			i_ = i + 1
			print(f"{i_} - {clients[i]}")
		print("**********************")

		if addr not in clients:
			clients.append(addr)

		itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
		print('[!] Данные, которые пришли от "SERVER":')
		print("****************************")
		print("Время: ", itsatime)
		print("****************************")
		print("["+addr[0]+"]=["+str(addr[1])+"]=["+itsatime+"]/",end="")
		print(data.decode("utf-8"))

		for client in clients:
			if addr != client:
				s.sendto(data,client)

		print("\n\n--------------------------------\n\n")
		i_r+= 1

	except:
		try:
			print("Последние данные с сервера",s.recvfrom(1024))
		except:
			pass
		finally:
			print("\n[!] Сервер разбился")
			quit = True
			input()
		
s.close()