#! -*- coding:utf-8 -*-
import os
from uiautomator import device as d 

os.environ["ANDROID_HOME"] = "/Users/liaozongmeng/adt-bundle-mac-x86_64-20140702/sdk"

def checkLock():
	'''检查手机是否有密码'''
	d.screen.off()
	d.screen.on()
	d(resourceId="android:id/glow_pad_view").swipe.down()
	return True


if __name__ == "__main__":
	print checkLock()
