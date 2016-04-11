import socket
import sys
import json
import time


def tcpSend(str2send, ip="127.0.0.1", port=11899):
	HOST, PORT = ip, port
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


cmd_wifi_connect = json.dumps({
	"CMD": "CONNECT_WIFI",
	"SSID": "dd-wrt_2.4g",
	"KEY": "13817486091"
	})
cmd_get_wifi_info = json.dumps({
	"CMD": "GET_WIFI_INFO"
	})
cmd_vib_test = json.dumps({
	"CMD": "VIB_TEST"
	})
cmd_set_paras = json.dumps({
	"CMD": "SET_VIB_PARAS",
	"AVR_TIME": 2000,
	"AVR_COUNT": 20
	})
cmd_test_no_vib = json.dumps({
	"CMD": "TEST_NO_VIB"
	})


# print tcpSend(cmd_wifi_connect)
# print tcpSend(cmd_get_wifi_info)
# print tcpSend(cmd_set_paras, "192.168.1.151")
print tcpSend(cmd_vib_test, "192.168.1.151")