# biliffm4s: Android哔哩哔哩缓存视频合并  

## 简介  

`biliffm4s`是`bilibili-ffmpeg-m4s(to-mp4)`的缩写.顾名思义,该项目提供了一个Python库,将Android手机哔哩哔哩缓存的视频(为`.m4s`)格式转化为`.mp4`格式.文件转化功能由`ffmpeg`实现,见[github链接](https://github.com/FFmpeg/FFmpeg)    
项目已经发布在PyPi上.因此,使用`pip install biliffm4s`即可使用.  
> 注:`ffmpeg.exe`已经包含在了项目中,因此可以开箱即用.暂时只支持Windows.  #TODO: 其它环境的兼容  

## 使用  

使用非常简单: 调用`biliffm4s`唯一提供的函数`convert()`即可.  
`convert`接受三个参数:  

- `video`: 输入的视频`.m4s`文件.该项缺省值为`video.m4s`,即相对路径下的哔哩哔哩缓存视频文件的缺省名称.可省略`.m4s`后缀名  
- `audio`: 输入的音频`.m4s`文件.该项缺省值为`audio.m4s`,即相对路径下的哔哩哔哩缓存音频文件的缺省名称.可省略`.m4s`后缀名  
- `output`: 输出的`.mp4`文件文件名.该项缺省值为`output.mp4`.可省略`.mp4`后缀名  

函数的返回值是`bool`,表示转换的成功与否.  

*示例:*  
```python
import biliffm4s

biliffm4s.convert('video.m4s', 'audio.m4s', 'result.mp4') # 将video.m4s和audio.m4s合并为result.mp4  
biliffm4s.convert(output='result2') # 将video.m4s和audio.m4s合并为result2.mp4 
biliffm4s.convert() # 将video.m4s和audio.m4s合并为output.mp4  
```

## 如何获取Android设备缓存的`.m4s`文件  

按照以下步骤进行操作:  

1. 将视频缓存到你的Android设备上  
2. 使用数据线将其链接至电脑,并进入`USB文件传输`模式  
3. 访问`\Android\data\tv.danmaku.bili\download`路径  
4. 你会看到一堆以数字命名的文件夹,每个文件夹都是一个缓存的视频.通过文件大小和时间判断对应的缓存视频  
5. 至对应文件夹的最深层次处,你会看到`video.m4s`,`audio.m4s`,`index.json`文件,分别对应哔哩哔哩视频的视频,音频和弹幕.拷贝两个`.m4s`到你的电脑上  

> 如果你使用的是哔哩哔哩概念版,那路径为`\Android\data\com.bilibili.app.blue\download`
