import socket
import sys
import json


def tcpSend(str2send):
	HOST, PORT = "192.168.1.152", 12580
	# Create a socket (SOCK_STREAM means a TCP socket)
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
	    # Connect to server and send data
	    sock.connect((HOST, PORT))
	    sock.sendall(str2send + "\n")
	    # Receive data from the server and shut down
	    received = sock.recv(1024)
	    return received
	finally:
	    sock.close()


cmd_set_avr_num = json.dumps({
	"CMD": "SET_AVR_NUM",
	"NUM": 10
	})
cmd_sensor_on = json.dumps({
	"CMD": "SENSOR_ON",
	"SENSOR_TYPE": "TYPE_ACCELEROMETER"
	})
cmd_sensor_off = json.dumps({
	"CMD": "SENSOR_OFF",
	"SENSOR_TYPE": "TYPE_ACCELEROMETER"
	})
cmd_pull_sensor_data = json.dumps({
	"CMD": "PULL_DATA",
	"SENSOR_TYPE": "TYPE_ACCELEROMETER"
	})

print cmd_set_avr_num
print tcpSend("SET_CHECK_ACC")
