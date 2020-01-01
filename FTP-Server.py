#install pyftpdlib library module and pip before start\
#apt install pip && apt install pip3
#pip install ftpdlib

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("mawan", "nevtik", "/home/username", perm="elradfmw") #You can use permission as you wish
authorizer.add_user("github", "12345", "/home/username", perm="elradfmw")
authorizer.add_anonymous("/home/username", perm="elradfmw") #For anonymous (Guest) user

handler = FTPHandler
handler.authorizer = authorizer

host, port = input("Input Host : "),int(input("Input Port[21] :"))
server = FTPServer(('host','port'), handler) 
server.serve_forever()
