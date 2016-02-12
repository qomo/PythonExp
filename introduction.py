#! -*- coding:utf-8 -*-

# 环境搭建
"""
- Anaconda
	- https://www.continuum.io/downloads
	- Spyder
"""

# 参考资料
"""
- 最好的参考资料是官方的document
- Python简明教程
	http://bcmi.sjtu.edu.cn/~zhaohai/ptm2012/data/byteofpython_chn.pdf
- Python科学计算
"""

# 获取帮助
"""
- Ipython --- help
- Google
"""

# 打个招呼
print "hello python!"

# 变量类型

## 内置变量类型
a = 1
print a, " is ", type(a)
a = 1.1
print a, " is ", type(a)
a = "1.1"
print a, " is ", type(a)
a = True
print a, " is ", type(a)
a = 1.1 + 1.1j
print a, " is ", type(a)
a = 111111111111111111111111111111111111111111
print a, " is ", type(a)

## 类型转换
print (1.1), int(1.1), str(1.1), bool(1.1)
print type(1.1), type(int(1.1)), type(str(1.1)), type(bool(1.1))

## 容器类型
"""
- List
- tuple
- dictionary
"""
list_data = [1, 1.1, "1.1", True]
print list_data
print list_data[1:3]
list_data[2] = "1.2"
print list_data

tuple_data = (1, 1.1, "1.1", True)
print tuple_data
print tuple_data[1:3]
# tuple_data[2] = "1.2"

dic_data = {"name": "lzm", "age": 18, "is_fighter": True}
print dic_data
print dic_data["is_fighter"]
dic_data["is_single"] = True
print dic_data

## ndarray
"""
详见demo_cv.py 
"""

# 控制语句

## IF 
import random
rdnum = random.random()
if rdnum<0.4:
	print "random num is: ", rdnum, "---", rdnum, " < 0.4"
elif rdnum>=0.4 and rdnum < 0.8:
	print "random num is: ", rdnum, "---", "0.4 <= ", rdnum, " < 0.8"
else:
	print "random num is: ", rdnum, "---", "0.8 <= ", rdnum

## FOR
list_data = range(10)
for i in list_data:
	print i

## WHILE
i = 10
while i > 0:
	if i == 5:
		i = i - 1
		continue
	if i == 2:
		break
	print i
	i = i - 1

## continu break

# 函数
def fib(n):
	'''get a list of fibnacci series to n'''
	a, b = 0, 1
	result = []
	while a<n:
		result.append(a)
		a, b = b, a+b 
	return result

print fib(10)

# 类 
class cat():
	"""class of cat"""
	def __init__(self, name, color):
		self.name = name
		self.color = color

	def meow(self):
		print "meow! I'm a ", self.color, " cat..."
white_cat = cat("wc", "white")
black_cat = cat("bc", "black")
white_cat.meow()
black_cat.meow()

# 文件读写
f = open("filetmp.txt", "a+")
f.seek(0)
print f.read()
f.write("This is a test\n")
f.close()

# 库
"""
导入库函数的两种方式
- import numpy
- from numpy import *
- from numpy import sqrt, pi

常用库
- numpy 
- scipy
- matplotlib
- cv2
- ctypes
......
"""

# opencv 例子
"""
- 直线识别 
- 人脸识别
"""