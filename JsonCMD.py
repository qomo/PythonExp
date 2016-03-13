import socket
import sys
import json
import time


def tcpSend(str2send):
	HOST, PORT = "127.0.0.1", 12580
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
	"NUM": 20
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
cmd_wifi_connect = json.dumps({
	"CMD": "CONNECT_WIFI",
	"SSID": "dd-wrt_2.4g",
	"KEY": "13817486091"
	})
cmd_get_wifi_info = json.dumps({
	"CMD": "GET_WIFI_INFO"
	})
cmd_play_music = json.dumps({
	"CMD": "PLAY_MUSIC"
	})
cmd_stop_music = json.dumps({
	"CMD": "STOP_MUSIC"
	})

def test_sensor(sensor_type):
	cmd_sensor_on = json.dumps({
		"CMD": "SENSOR_ON",
		"SENSOR_TYPE": sensor_type
		})
	cmd_sensor_off = json.dumps({
		"CMD": "SENSOR_OFF",
		"SENSOR_TYPE": sensor_type
		})
	cmd_pull_sensor_data = json.dumps({
		"CMD": "PULL_DATA",
		"SENSOR_TYPE": sensor_type
		})
	print tcpSend(cmd_sensor_on)
	print tcpSend(cmd_pull_sensor_data)
	print tcpSend(cmd_sensor_off)


# test_sensor("TYPE_ACCELEROMETER")
# test_sensor("TYPE_GYROSCOPE")
# test_sensor("TYPE_MAGNETIC_FIELD")
test_sensor("TYPE_LIGHT")
# print tcpSend(cmd_wifi_connect)
# print cmd_set_avr_num
# print tcpSend(cmd_sensor_on)
# time.sleep(0.5)
# print tcpSend(cmd_pull_sensor_data)
# print tcpSend(cmd_sensor_off)
# print tcpSend(cmd_set_avr_num)
# print tcpSend("SET_CHECK_ACC")
# print tcpSend(cmd_get_wifi_info)
# print tcpSend(cmd_play_music)
# time.sleep(10)
# print tcpSend(cmd_stop_music)