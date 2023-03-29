#get machine info

import socket

def get_machine_info():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print "Host name: %s" %hostname
    print "IP: %s" %ip

if __name__ == '__main__':
    get_machine_info()
