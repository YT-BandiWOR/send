settings_file_1 = "set\\host.txt"
settings_file_2 = "set\\port.txt"
settings_file_3 = "set\\host_server.txt"


def get_host(file=settings_file_1):
	return str(open(file, 'r').read())


def get_port(file=settings_file_2):
	return int(open(file, 'r').read())


def get_host_server(file=settings_file_3):
	return str(open(file, 'r').read())