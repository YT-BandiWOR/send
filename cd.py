import os

def CreateDir():
	print("""\nЗапущено меню настроек
1. Нажмите сочетание клавиш Win + R
2. В открывшемся окне напишите "cmd"
3. Нажмите на кнопку "ОК"
4. В консоле, которая открылась напишите "ipconfig"
5. Нажмите на клавишу "Enter"
6. Найдите данное поле:
   IPv4-адрес. . . . . . . . . . . . : *ваш адрес*

   !Внимание! Если у вас несколько таких полей, то впишите данные только с самого верхнего
7. Вместо *ваш адрес написаны цифры*, их запишите куда-нибудь.
""")
	host = input("Напишите эти цифры с точками сюда;\nIPv4-адрес ")
	try:
		os.mkdir("set")
	except:
		pass
	open("set\\host.txt", 'w').write(host)
	open("set\\port.txt", 'w').write("9090")
	print("Если у Вас всё заработало, то всё отлично, если нет, то поищите в интернете \"Как узнать свой IPv4-адрес\", и перейдите в папку \"set\", откройте файл \"host.txt\", запишите в него свой IPv4-адрес\n\n")

	print("Уже выполнено 50% работы.")

	host_host = input("Выполните процедуру по поиску IPv4-адреса на ПК, где будет запущен сервер, и впишите его сюда\nIPv4-адрес ")
	open("set\\host_server.txt", 'w').write(host_host)

	print("Успешно!")