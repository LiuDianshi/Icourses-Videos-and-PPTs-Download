# Icourses-Videos-and-PPTs-Download
## 爱课程视频以及课件下载

这个啰嗦的文件的目录：说明-->最新版本更新日志-->使用教程

### 说明：

本程序可用于下载**爱课程**网站上的视频和课件资源，除此之外还支持课程界面的『习题作业』、『测试试卷』等所有课程资源下载。

#### 特点：

1.作者是个门外汉，所以代码写得特别烂，但同时也在不断优化

2.保持不断更新和修复bug

3.已发布[Release](https://github.com/LiuDianshi/Icourses-Videos-and-PPTs-Download/releases)，直接下载运行即可 ，无需安装Python

4.如果这个程序帮到了你，欢迎star，如果你想请我吃个手抓饼可以扫以下二维码😊
![](http://ww1.sinaimg.cn/large/006y4Bmtly1g03wzdcmmej30m80gowli.jpg)

---

### 更新日志：

V1.3.9.2( 2020.3.7 对应release为v1.2.3)

好久不见！
修复 近期（由于爱课程网页版前端更新所造成的）无法使用的问题以及一些其他的小问题

[点我](https://github.com/LiuDianshi/Icourses-Videos-and-PPTs-Download/releases/tag/v1.2.3)下载

---


V1.3.9.1( 2019.4.9 对应release为v1.2.2)

修复 在Windows下使用时会出现的改名乱码问题

[点我](https://github.com/LiuDianshi/Icourses-Videos-and-PPTs-Download/releases/tag/v1.2.2)下载

---

V1.3.9( 2019.2.18 对应release为v1.2.1)

新增检查更新功能，优化了PPT模式解析时文件的命名方式及极个别情况下资源不完整的问题

[点我](https://github.com/LiuDianshi/Icourses-Videos-and-PPTs-Download/releases/tag/v1.2.1)下载

---

V1.3.8( 2019.2.12 对应release为v1.2.0)

修复了若干bug，优化了文件改名的逻辑

[点我](https://github.com/LiuDianshi/Icourses-Videos-and-PPTs-Download/releases/tag/v1.2.0)下载

---


V1.3.7( 2019.1.22 对应release为v1.1.0)

终于写好了图形界面了，再也不用对着丑陋的命令行操作了！

[点我](https://github.com/LiuDianshi/Icourses-Videos-and-PPTs-Download/releases/tag/v1.1.0)下载


## 使用教程：

#### 写在前面：
1.如果以下教程无法正常运行可选择从源代码运行：[点我](https://github.com/LiuDianshi/Icourses-Videos-and-PPTs-Download/blob/master/从源代码运行.md)

2.为保证可用，Github上提供的将暂时保持在V1.3.7版本，直至最新版本的程序趋于稳定，如果需要最新版本的源代码可在release处下载。

3.绝大多数情况下PDF模式解析的资源是完整的，如果PPT模式解析出错或资源不完整，可尝试PDF方式解析或在您方便时给我反馈。

### 在Windows上运行：

#### 1.下载

- 前往Github的Release的页面下载已经打包好的程序，请下载最新版本

  ![](https://ws1.sinaimg.cn/large/006y4Bmtly1fyzlmxg3ebj313g0kj40l.jpg)

  ![](https://ws1.sinaimg.cn/large/006y4Bmtly1fyzlmxn6onj30xa0dsjsk.jpg)


- 双击运行，会出现一个黑框和一个白框
[![kkcSKg.md.png](https://s2.ax1x.com/2019/01/22/kkcSKg.md.png)](https://imgchr.com/i/kkcSKg)

  按照提示输入相关信息即可，注意填入保存地址和课程链接后都要按一下下面的确认按钮。开始运行后系统可能会显示程序未响应，耐心等待即可。

  ![kkctMD.png](https://s2.ax1x.com/2019/01/22/kkctMD.png)
   一段时间后会出现如图所示的界面，此时即下载完成。
   [![kkgM6S.png](https://s2.ax1x.com/2019/01/22/kkgM6S.png)](https://imgchr.com/i/kkgM6S)
   如果程序运行出现错误，请将黑框截图和弹出窗口截图反馈给我，我的联系方式在文末。

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

  如`http://www.icourses.cn/sCourse/course_5976.html`也就是说只能下载爱课程的课程资源。

- 输入保存地址的例子`D:\学习资料\爱课程`，不能有空格，建议直接到文件管理器中复制路径，如图

  ![](https://ws1.sinaimg.cn/large/006mO5TVly1fp21qd08nwj30wm0640t6.jpg)

- 保存路径应尽可能简单，比如`D:\爱课程`，建议不要有一些乱七八糟的符号

- 不能下载中国大学Mooc资源不能下载中国大学Mooc资源不能下载中国大学Mooc资源

- 如果以上操作都正确但无法下载，请联系我

- 本程序仅用于个人学习使用，如果侵害了相关人员的权益，请及时删除

### 在Linux/macOs上运行:

下载运行环节，与Windows基本相同

下载完成后，如下图所示
![](https://ws1.sinaimg.cn/large/006y4Bmtly1fyzn8wga1ej319k0u8qdl.jpg)

在终端中打开该路径，输入`chmod 777 IcourseDownloade_macOS_1.0.0`,再输入`./IcourseDownloade_macOS_1.0.0`即可运行按照提示输入信息即可。如下图所示
![](https://ws1.sinaimg.cn/large/006y4Bmtly1fyzneo2j57j30vo0p4q6k.jpg)

运行结束后会在输入的路径内产生三个文件：

![](https://ws1.sinaimg.cn/large/006y4Bmtly1fvvknkescbj316s0o8dpp.jpg)

根据需要复制相应的下载链接至下载软件进行下载，下载好的文件名字是乱的：

![](https://ws1.sinaimg.cn/large/006y4Bmtly1fvvknkpnqoj316s0t64ge.jpg)

此时在终端切换到该路径下，输入`chmod 777 change_name.sh`然后输入`./change_name.sh`即可改名

![](https://ws1.sinaimg.cn/large/006y4Bmtly1fvvknlbr8aj30vo0p4gmp.jpg)

![](https://ws1.sinaimg.cn/large/006y4Bmtly1fvvknl32gkj316s0t6wwj.jpg)


Python小白，自娱自乐，大神勿喷，手动/doge

QQ : 1833727822





