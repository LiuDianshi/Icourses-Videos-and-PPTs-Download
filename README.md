# Icourses-Videos-and-PPTs-Download
## 爱课程视频以及课件下载

这个啰嗦的文件的目录：说明、更新日志、使用教程

### 说明：

本程序可用于下载**爱课程**网站上的视频和课件资源，除此之外还支持课程界面的『习题作业』、『测试试卷』等所有课程资源下载。

#### 特点：

1.作者是个门外汉，所以代码写得特别烂，但同时也在不断优化

2.保持不断更新

3.如果Github无法下载，可[点我](https://www.jianguoyun.com/p/DQDj3L0Q9tjLBhi7gno)从坚果云下载

4.如果这个程序帮到了你，欢迎star

### 更新日志：

V1.3.6.1(2018.12.26)

好久没更新了，因为前段时间去考了个研(ಠ_ಠ)

因为程序默认调用的是移动端API，最近收到反馈说课程资源不完整，疑似这个API的锅，已经禁用它了，也就是说暂时无法解析PPT格式的课件了(后续会想办法支持），但解析到的资源是完整的。

下一阶段目标：PPT课件，程序打包，GUI

V1.3.6(2018.11.7)

**重要说明**：根据部分同学反映程序无法正常运行(表现为无故自动结束运行)，这个bug在我这边没有复现所以无法发现根本原因，疑似是部分地区无法正常访问新版本所调用的爱课程的API所致。该版本的程序支持解析PPT课件40秒若无结果自动切换至解析PDF课件的方法。

V1.3.5(2018.10.23)

修复了新的解析方式无法获取完整资源的bug

V1.3.4(2018.10.15)

现已支持PPT文件下载，感谢@爱乒乓和电视做靠谱儿的事儿，最大限度地保持官网课程资源的原貌，因未经严格测试，所以并未移除原解析pdf课件的功能，如果解析PPT文件失效会自动调用原解析文件。本次使用教程变动较大，建议阅读。

V1.3.3(2018.10.4)

新增Linux和macOS的支持，目前已支持在三大平台运行，具体操作看下面的使用教程。

V1.3.2(2018.9.30)

修复了某些情况下无法改名和下载的bug

V1.3.1(2018.9.23)

可自动生成两个文本文件`批量下载链接.txt`和`分条下载链接.txt`，可根据需要批量下载或单个文件下载

V1.3(2018.9.15)

新增自动生成改名程序`change_name.cmd`，双击即可修改文件名，可随时离线修改。

V1.2.6(2018.9.14)

修复了某些课程无法改名的bug

V1.2.5(2018.8.19)

增加爱课程页面的“习题作业”和“测试试卷”资源的下载（如下图），目前已支持爱课程所有课程所有资源的下载。

V1.2.4(2018.8.6)

彻底修复了抓取不全的bug(我用人格担保 /doge)，修复了部分文件不能改名的bug，新增下载课程列表里的“其他资源”的功能(实验性，可能不稳定)。

下一个版本会把改名功能单独独立出来。

V1.2.3(2018.7.27)

修复了抓取不全的bug,增加提示信息。

V1.2.2(2018.7.16)

经反馈，已知的从爱课程网页获取资源的解析方式有两种，目前的版本已经包含了这两种解析方式，但不能确认是否存在其他的解析方式，如果在使用过程中发现解析失败，请将课程的链接以各种方式反馈给我。

V1.2.1(2018.6.7)

近日爱课程更改了前端逻辑，使源程序失效，具体表现为`下载链接.txt`文件为空，2.1版本已修复

其运行方法与`V1.2.0`基本一致，请参考`V1.2.0`的运行方法。

已知Bug：某些课程的文件会出现无法改名的bug，待修复。

V1.2（2018.4.20）

0.程序完全重写

1.因为爱课程限制，下载速度特别慢，故把原程序的下载功能取消，改为给出下载链接，由用户选择下载工具进行下载

2.新增改名功能



## 使用教程：

### 在Windows上运行：

### 简略无废话版：

如下：

>1. 安装Python(建议Python3.5以上)，在安装时选准从选择`将Python添加至环境变量`
>2. 下载或clone
>3. 安装`bs4`,`requests`,`lxml`
>4. 在`Powershell`或者`cmd`中运行`run.py`，或者直接电机`start.cmd`文件，按照提示输入信息
>5. 此时会在输入的路径中生成两个文本文件`批量下载链接.txt`和`分条下载链接.txt`，下载链接均在其中，可根据需要复制到下载软件中下载，同时会生成一个改名文件`change_name.cmd`，双击即可改名
>6. 将`change_name.cmd`改名文件复制到刚刚下载好的课程资源文件目录中，双击即可修改



### 详细版：

#### 1.安装Python3.5及以上

如果没有安装Python的话，需要先安装Python

推荐前往[Python官网](https://www.python.org/)下载

如果下载的是`Python3.6`的版本，下载完成后得到一个名为`python-3.6.exe`的文件，双击打开，界面如图所示：

![](https://ws1.sinaimg.cn/large/006mO5TVly1fp20mb2nfxj30n40e8aef.jpg)

一定要把那个`Add Python 3.6 to PATH `选项打上勾。

等进度条跑完，就完成了Python的安装。

#### 2.运行

###### 安装第三方库

本程序使用的第三方库有：`requests`,`BeautifulSoup`,`lxml`，

按下`Win`+`R`键在弹出的框中输入`cmd`打开命令提示符，依次输入:

```powershell
pip install requests
pip install bs4
pip install lxml
```

###### 下载源代码并运行

![](https://ws1.sinaimg.cn/large/006mO5TVly1fp212zr5n9j312v0gkmza.jpg)



之后会下载一个`.zip`的压缩包，将其中的内容解压到桌面上会得到如下文件：

![](https://ws1.sinaimg.cn/large/006y4Bmtly1fw88z4g95hj30p405ygm7.jpg)

在空白处按住`Shift`单击右键，选择`在此处打开Powershell窗口`(只有较新的win10版本才有该选项，其他Windows可选择`在Cmd中打开`，输入`python run.py`即可运行。也可以直接双击`start.cmd`运行。

运行程序时，输入保存地址、课程地址

![](https://ws1.sinaimg.cn/large/006y4Bmtly1fw892ureyrj312q05gq5c.jpg)

这是在保存地址内会出现`下载链接.txt`文件，里面为该课程所有视频、课件的下载地址，可将链接复制后用第三方下载工具如迅雷下载

同时也会生成一个`change_name.cmd`文件用于改名

如下图所示

![](https://ws1.sinaimg.cn/large/006y4Bmtly1fvanz4c50uj30f8050aa2.jpg)

例如随便选择几个该课程的课件地址复制

![](https://ws1.sinaimg.cn/large/006y4Bmtly1fw894r0qr3j30tp0hgwp7.jpg)

打开迅雷即可下载

![](https://ws1.sinaimg.cn/large/006y4Bmtly1fw896acb5gj30x90m3786.jpg)

下载后的文件名字是乱的

![](https://ws1.sinaimg.cn/large/006y4Bmtly1fw897ccbpqj30vg0llter.jpg)

双击`change_name.cmd`后即可自动改名

![](https://ws1.sinaimg.cn/large/006y4Bmtly1fw89cqit04j30vf0lmjw5.jpg)



#### 3.运行注意事项

- 输入程序的链接格式为`http://www.icourses.cn/sCourse/course_****.html`，

  如`http://www.icourses.cn/sCourse/course_5976.html`

- 输入保存地址的例子`D:\学习资料\爱课程`，不能有空格，建议直接到文件管理器中复制路径，如图

  ![](https://ws1.sinaimg.cn/large/006mO5TVly1fp21qd08nwj30wm0640t6.jpg)

- 如果以上操作都正确但无法下载，请联系我

- 本程序仅用于个人学习使用，如果侵害了相关人员的权益，请及时删除

### 在Linux/macOs上运行:

### 简略无废话版：

如下：

> 1. 安装Python(建议Python3.5以上)
> 2. 下载或clone
> 3. 安装`bs4`,`requests`,`lxml`三个Python库
> 4. 修改配置文件`config.py`，给予权限后运行`start.sh`，或者直接运行run.py，按照提示输入信息
> 5. 此时会在输入的路径中生成两个文本文件`批量下载链接.txt`和`分条下载链接.txt`，下载链接均在其中，可根据需要复制到下载软件中下载，同时会生成一个改名文件`change_name.sh`，给予权限并运行即可改名



### 详细版：

#### 1.安装Python3.5及以上及第三方库

在不同的Linux发行版上安装Python3的方法也各不相同，请自行查询

在macOS上安装Python推荐使用`homebrew`

安装三个第三方库的方法也与Windows一样

### 2.下载源代码并解压

与Windows相同

### 3.运行

在终端内切换到解压目录

打开config.py文件修改配置，将`mode`的值改为1

![](https://ws1.sinaimg.cn/large/006y4Bmtly1fw88fhft3nj30zk0rwq4k.jpg)

在终端输入`chmod 777 start.sh`给予权限，然后输入`./start.sh`运行，或者直接运行`run.py`如下图：![](https://ws1.sinaimg.cn/large/006y4Bmtly1fw88j4jx72j30vo0p4di3.jpg)

按照提示输入信息即可。

如果PPT文件解析失败会自动调用原解析文件解析pdf课件

运行结束后会在输入的路径内产生三个文件：

![](https://ws1.sinaimg.cn/large/006y4Bmtly1fvvknkescbj316s0o8dpp.jpg)

根据需要复制相应的下载链接至下载软件进行下载，下载好的文件名字是乱的：

![](https://ws1.sinaimg.cn/large/006y4Bmtly1fvvknkpnqoj316s0t64ge.jpg)

此时在终端切换到该路径下，输入`chmod 777 change_name.sh`然后输入`./change_name.sh`即可改名

![](https://ws1.sinaimg.cn/large/006y4Bmtly1fvvknlbr8aj30vo0p4gmp.jpg)

![](https://ws1.sinaimg.cn/large/006y4Bmtly1fvvknl32gkj316s0t6wwj.jpg)


Python小白，自娱自乐，大神勿喷，手动/doge

QQ : 1833727822

微博：[@_刘点石](http://weibo.com/u/6000289349?refer_flag=1001030201_)

博客：[点石成铁](http://liudianshi.top)





