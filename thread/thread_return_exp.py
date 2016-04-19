#! -*- coding:utf-8 -*-
import threading
from random import randint
import time

class CmdThread(threading.Thread):
	"""多线程例子，能够将执行结果返回"""
	def __init__(self, tn):
		threading.Thread.__init__(self)
		self.__tn = tn
		print "Initial ", self.__tn
		self.__ri = None

	def run(self):
		self.__ri = randint(0,10)
		time.sleep(self.__ri)
		print "In ", self.__tn, " run(): ri = ", self.__ri

	def getRandint(self):
		return self.__ri


if __name__ == "__main__":
	t1 = CmdThread("t1")
	t2 = CmdThread("t2")
	t1.start()
	t2.start()
	print t1.getRandint()
	print t2.getRandint()