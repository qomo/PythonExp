#Python例程库
>收集有用的python代码

## opencv_demo —— 一个opencv demo  

### 环境搭建  

参考：  
> http://www.mobileway.net/2015/02/14/install-opencv-for-python-on-mac-os-x/

要点：  
1、在`brew install opencv`时若遇到问题  
> Error: Failed to download resource "gnuradio--numpy" 

请升级你的brew,`sudo brew upgrade`  
参考：  
> https://github.com/metacollin/homebrew-gnuradio/issues/48  

2、最后请按提示配置环境变量，以免opencv与numpy版本不一致导致的import cv2错误
