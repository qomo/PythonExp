import time
from SimpleXMLRPCServer import SimpleXMLRPCServer

def add(x, y):
	return x+y

def dell(x, y):
	time.sleep(x)
	return x-y

def stopServer():
	server.server_close()

server = SimpleXMLRPCServer(("127.0.0.1", 8000))
print "Listening on port 8000..."
server.register_function(add, "add")
server.register_function(dell, "dell")
server.register_function(stopServer, "stopServer")

server.serve_forever()