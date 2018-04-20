# Icourses-Videos-And-PDF-Download
## 爱课程MP4格式视频以及PDF课件下载

## V2.0（2018.4.20）

ChangeLog:

0.程序完全重写

1.因为爱课程限制，下载速度特别慢，故把原程序的下载功能取消，改为给出下载链接，由用户选择下载工具进行下载

2.新增改名功能

演示如下：

#### 1.安装Python3.6

安装方式见`V1.0`运行教程

#### 2.在浏览器中登录爱课程

安装方式见`V1.0`运行教程

#### 3.下载并运行`V2.0`程序源代码

按照`V1.0`运行教程的说明，安装第三方库，下载源代码，解压，进入`SRC`，`v2.0`，即可看到`Icourse.py`文件，在空白处按住`Shift`单击右键，选择`在此处打开Powershell窗口`，输入`python Icourse.py`即可运行。

效果如图：

运行程序，输入保存地址、课程地址

![](https://ws1.sinaimg.cn/large/006y4Bmtly1fqjfkz2vz7j30xz056mxo.jpg)

这是在保存地址内会出现`下载链接.txt`文件，里面为该课程所有视频、课件的下载地址，可将链接复制后用第三方下载工具如迅雷下载

例如将该课程所有的课件地址复制，打开迅雷即可下载

![](https://ws1.sinaimg.cn/large/006y4Bmtly1fqjfockf7lj30sd0kkjvp.jpg)

![](https://ws1.sinaimg.cn/large/006y4Bmtly1fqjfok1vbzj30yc0nbqaw.jpg)

下载后的文件名字是乱的

![](https://ws1.sinaimg.cn/large/006y4Bmtly1fqjfq1dszij31540mlgpk.jpg)

可以使用程序自带的改名功能，只需在刚才的窗口中输入`Y`或者`y`，按下回车键即可

![](https://ws1.sinaimg.cn/large/006y4Bmtly1fqjfqonq43j314u0m1wia.jpg)


## V1.0
### 使用方法：

#### 1.安装Python3.6

本程序由Python3.6.4编写，因此首先需要安安装Python

[Python官网](https://www.python.org/)

[Python3.6.4安装包下载](https://www.python.org/ftp/python/3.6.4/python-3.6.4.exe)

下载完成后得到一个名为`python-3.6.4_2.exe`的文件，双击打开，界面如图所示：

![](https://ws1.sinaimg.cn/large/006mO5TVly1fp20mb2nfxj30n40e8aef.jpg)

一定要把那个`Add Python 3.6 to PATH `选项打上勾。

此时完成了Python的安装。

#### 2.运行前准备

打开浏览器，打开[爱课程](http://www.icourses.cn/home/)官网,搜索自己想要下载的课程，比如搜索`数据结构`，如图

![](https://ws1.sinaimg.cn/large/006mO5TVly1fp21b46ugbj318l0eidkx.jpg)

此时一定要点击`登录`进行登录操作，否则将无法下载。

登录之后复制地址栏的地址即可。

#### 3.运行

##### 方法一：复杂方法

###### 1.安装第三方库

本程序使用的第三方库有：`requests`,`BeautifulSoup`,`lxml`，

按下`Win`+`R`键在弹出的框中输入`cmd`打开命令提示符，依次输入:

```powershell
pip install requests
pip install bs4
pip installer lxml
```

###### 2.下载源代码并运行

![](https://ws1.sinaimg.cn/large/006mO5TVly1fp212zr5n9j312v0gkmza.jpg)



之后会下载一个`.zip`的压缩包，将其中的内容解压到桌面上会得到如下文件：

![](https://ws1.sinaimg.cn/large/006mO5TVly1fp217h2eeuj30ob035q2x.jpg)

依次点击`SRC`，`V 1.0`，`download.py`即可

##### 方法二：简单方法

无需安装第三方库，相同的方法下载`.zip`文件并解压后，打开`Packaged`，`V 1.0`，`download.exe`即可。

#### 4.运行注意事项

- 下载前请一定要在浏览器中登录爱课程

- 输入程序的链接格式为`http://www.icourses.cn/sCourse/course_****.html`，

  如`http://www.icourses.cn/sCourse/course_5976.html`

- 输入保存地址的例子`D:\学习资料\爱课程`，建议直接到文件管理器中复制路径，如图

  ![](https://ws1.sinaimg.cn/large/006mO5TVly1fp21qd08nwj30wm0640t6.jpg)

- 如果以上操作都正确但无法下载，请联系我


Python小白，自娱自乐，大神勿喷，手动/doge

QQ : 1833727822

微博：[@_刘点石](http://weibo.com/u/6000289349?refer_flag=1001030201_)

博客：[点石成铁](liudianshi.top)





