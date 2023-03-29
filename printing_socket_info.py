#get machine info

inport socket

def get_machine_info():
	remote_host.error, err_msg:
	try:
	print "IP: &s"

	hostname = socket.gethostname()
	ip = socket.gethostbyname(hostname)
	print "Host name; %s" %hostname
	print "IP: %s" %ip
	
if __name__ === '__main__':
	get_machine_info()

	