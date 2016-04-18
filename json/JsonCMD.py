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
cmd_sensor_test = json.dumps({
	"CMD": "SENSOR_TEST",
	"SENSOR_TYPE": "TYPE_GYROSCOPE",
	"AVR_TIME": 5000,
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
	cmd_get_realtime_data = json.dumps({
		"CMD": "GET_SENSOR_VALUE",
		"SENSOR_TYPE": sensor_type
		})
	print tcpSend(cmd_sensor_on)
	print tcpSend(cmd_pull_sensor_data)
	print tcpSend(cmd_get_realtime_data)
	print tcpSend(cmd_get_realtime_data)
	print tcpSend(cmd_get_realtime_data)
	print tcpSend(cmd_get_realtime_data)
	print tcpSend(cmd_sensor_off)

def get_sensor_avr(sensor_type, avr_time):
	cmd_get_avr_value = json.dumps({
		"CMD": "GET_SENSOR_AVR_VALUE",
		"SENSOR_TYPE": sensor_type,
		"AVR_TIME": avr_time
		})
	print tcpSend(cmd_get_avr_value)

avr_times = [100, 1000, 2000, 3000]
sensor_types = ["TYPE_ACCELEROMETER", "TYPE_GYROSCOPE", "TYPE_MAGNETIC_FIELD", "TYPE_ORIENTATION"]

# get_sensor_avr("TYPE_PRESSURE", "1000")

# for sensor_type in sensor_types:
# 	for avr_time in avr_times:
# 		print sensor_type, " ", avr_time
# 		get_sensor_avr(sensor_type, avr_time)

get_sensor_avr("TYPE_GYROSCOPE_UNCALIBRATED", 4000)

# test_sensor("TYPE_ACCELEROMETER")
# test_sensor("TYPE_GYROSCOPE")
# test_sensor("TYPE_MAGNETIC_FIELD")
# test_sensor("TYPE_ORIENTATION")
# test_sensor("TYPE_LIGHT")
# test_sensor("TYPE_GYROSCOPE_UNCALIBRATED")
# print tcpSend(cmd_sensor_test)
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