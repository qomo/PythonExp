import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://127.0.0.1:8000/")
try:
	print proxy.add(0, 5)
except xmlrpclib.Fault as err:
	print "A fault occurred"
	print "Fault code: %d" % err.faultCode
	print "Fault string: %s" % err.faultString

try:
	print proxy.dell(0, 5)
except xmlrpclib.Fault as err:
	print "A fault occurred"
	print "Fault code: %d" % err.faultCode
	print "Fault string: %s" % err.faultString

try:
	print proxy.stopServer()
except xmlrpclib.Fault as err:
	print "A fault occurred"
	print "Fault code: %d" % err.faultCode
	print "Fault string: %s" % err.faultString