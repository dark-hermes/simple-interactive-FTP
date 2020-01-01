#install ftpflib library and pip before start 
#apt install python3-pip && pip install ftpdlib

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("mawan13", "130504", "Server", perm="elradfmw") #Change "Server" with your directory
authorizer.add_user("github","12345", "Server", perm="elradfmw") #You can change user permission as you wish
authorizer.add_anonymous("/home/username", perm="elradfmw") #For anonymous (Guest) user

handler = FTPHandler
handler.authorizer = authorizer

host, port = input("Input Host : "), int(input("Port : "))
server = FTPServer((host,port), handler)
server.serve_forever()
