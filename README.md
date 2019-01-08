# Icourses-Videos-and-PPTs-Download
## 爱课程视频以及课件下载

这个啰嗦的文件的目录：说明-->更新日志-->使用教程

### 说明：

本程序可用于下载**爱课程**网站上的视频和课件资源，除此之外还支持课程界面的『习题作业』、『测试试卷』等所有课程资源下载。

#### 特点：

1.作者是个门外汉，所以代码写得特别烂，但同时也在不断优化

2.保持不断更新

3.已发布[Release](https://github.com/LiuDianshi/Icourses-Videos-and-PPTs-Download/releases)，直接下载运行即可 ，无需安装Python

4.如果这个程序帮到了你，欢迎star

### 更新日志：

V1.3.6.2(2019.1.7)

恢复了PPT解析，可在运行时选择是否使用。

已发布[Release](https://github.com/LiuDianshi/Icourses-Videos-and-PPTs-Download/releases)(2019.1.8)，无需安装Python和第三方库，下载运行即可，详见下面的使用教程。

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

如果以下教程无法正常运行可选择从源代码运行：[点我](https://github.com/LiuDianshi/Icourses-Videos-and-PPTs-Download/blob/master/从源代码运行.html)

### 在Windows上运行：

#### 1.下载

- 前往Github的Release的页面下载已经打包好的程序

  ![](https://ws1.sinaimg.cn/large/006y4Bmtly1fyzlmxg3ebj313g0kj40l.jpg)

  ![](https://ws1.sinaimg.cn/large/006y4Bmtly1fyzlmxn6onj30xa0dsjsk.jpg)


- 双击运行

  按照提示输入相关信息即可，运行结束后或出错窗口会自动关闭(如果程序出现bug或者输入错误会造成闪退)

  ![](https://ws1.sinaimg.cn/large/006y4Bmtly1fyzm85sq36j30xz0hqab4.jpg)


- 运行结束后会在输入的目录内产生以下文件

  ![](https://ws1.sinaimg.cn/large/006y4Bmtly1fyzm9q1o7xj30y50jwq4e.jpg)

`批量下载链接.txt`和`分条下载链接.txt`为该课程所有视频、课件的下载地址，可将链接复制后用第三方下载工具如迅雷下载

同时也会生成一个`change_name.cmd`文件用于改名

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

下载运行环节，与Windows基本相同

按照提示输入信息即可。

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





