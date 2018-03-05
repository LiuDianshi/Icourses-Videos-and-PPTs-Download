import re
import urllib.request
from getURL import getURL
from multiprocessing.dummy import Pool as ThreadPool
from getLocation import getLocation


def main():
    title, file = getURL()
    exention = []
    for i in range(len(file)):
        a = re.findall(r'[mpd4f]{3}', str(file[i]))[0]
        exention.append(a)
    real_loc = getLocation()
    for i in range(len(file)):
        file_name = real_loc + title[i] + '.' + exention[i]
        try:
            print('正在下载:'+file_name)
            urllib.request.urlretrieve(file[i],file_name)
            continue
        except FileNotFoundError as e:
            print('保存位置出错，请联系开发者'+e)
        finally:
            pass


if __name__ == "__main__":
    print('欢迎使用爱课程视频、课件批量下载器')
    print('本程序由能源学院刘成金编写')
    print('下载的文件仅供学习使用，不得传播')
    print('并且请于24小时内将文件删除')
    print('否则一切后果自负，与程序编写者无关')
    print('*' * 20)
    print('**重要提醒**使用前请先在浏览器中登陆爱课程')
    main()
