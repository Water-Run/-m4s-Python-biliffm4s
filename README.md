# biliffm4s: Android哔哩哔哩缓存视频合并  

## 简介  

`biliffm4s`是`bilibili-ffmpeg-m4s(to-mp4)`的缩写.顾名思义,该项目提供了一个Python库,将Android手机哔哩哔哩缓存的视频(为`.m4s`)格式转化为`.mp4`格式.文件转化功能由`ffmpeg`实现,见[github链接](https://github.com/FFmpeg/FFmpeg)    
项目已经发布在PyPi上.因此,使用`pip install biliffm4s`即可使用.`biliffm4s`是即开即用的,不需要安装第三方依赖(如配置`ffmpeg`环境等).    
> 仅适配Windows 64位平台  

## 使用  

`biliffm4s`的使用非常简单:按需使用提供的`convert()`和`combine()`即可.  
具体使用见下:  

### `convert()`  
`convert`函数接受输入的音视频`.m4s`文件,合并并输出为`.mp4`.  
- 参数  
    - `video`: 输入的视频路径.后缀`.m4s`可以省略.缺省值为`video.m4s`  
    - `audio`: 输入的音频路径.后缀`.m4s`可以省略.缺省值为`audio.m4s`  
    - `output`: 输出的视频路径.后缀`.mp4`可以省略.缺省值为`output.mp4`  
- 返回值: `bool` 合并成功与否  

### `combine()`  
`convert`函数需要手动找到对应的`.m4s`,有时这并不够方便.`combine`函数提供了一种更简单的方式:只需要提供包含对应`video.m4s`和`audio.m4s`(哔哩哔哩的缓存视频文件夹始终是这两个名称)的文件夹路径即可,其会自动的进行查找并合并.  
> 在使用`combine()`时,确保路径下只有唯一的`video.m4s`和`audio.m4s`  
- 参数  
    - `directory`: 包含`video.m4s`和`audio.m4s`的文件夹路径  
    - `output`: 输出的视频路径.后缀`.mp4`可以省略.缺省值为`output.mp4`  
- 返回值: `bool` 合并成功与否  

*示例:*  
```python
import biliffm4s

biliffm4s.convert('video.m4s', 'audio.m4s', 'result.mp4') # 将video.m4s和audio.m4s合并为result.mp4  
biliffm4s.convert(output='result2') # 将video.m4s和audio.m4s合并为result2.mp4 
biliffm4s.convert() # 将video.m4s和audio.m4s合并为output.mp4  
biliffm4s.combine('sample') # 自动读取sample文件夹下的video.m4s和audio.m4s并合并为output.mp4
```

## 如何获取Android设备缓存的`.m4s`文件  

按照以下步骤进行操作:  

1. 将视频缓存到你的Android设备上  
2. 使用数据线将其链接至电脑,并进入`USB文件传输`模式  
3. 访问`\Android\data\tv.danmaku.bili\download`路径  
4. 你会看到一堆以数字命名的文件夹,每个文件夹都是一个缓存的视频.通过文件大小和时间判断对应的缓存视频  
5. 至对应文件夹的最深层次处,你会看到`video.m4s`,`audio.m4s`,`index.json`文件,分别对应哔哩哔哩视频的视频,音频和弹幕.拷贝两个`.m4s`到你的电脑上  

> 如果你使用的是哔哩哔哩概念版,那路径为`\Android\data\com.bilibili.app.blue\download`  
> 如果你使用的是`combine()`,直接复制\download路径下的对应子文件夹即可  
