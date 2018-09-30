# -*- coding: utf-8 -*-
"""爱课程资源下载"""

import requests
from bs4 import BeautifulSoup
import re
import json
import lxml
import os


def get_course_name(id):
    url = 'http://www.icourses.cn/sCourse/course_' + str(id) + '.html'
    result = requests.get(url)
    result.encoding = result.apparent_encoding
    soup = BeautifulSoup(result.text, 'lxml')
    name = soup.find('p', class_='pull-left')
    try:
        print('正在解析 ' + name.text + ' 课程资源')
    except:
        print('未找到该课程的信息，请确认输入的链接是否正确')
        exit()
    finally:
        pass


def get_html(id, loc):
    header = {
        'Accept':
        '*/*',
        'Accept-Encoding':
        'gzip, deflate',
        'Accept-Language':
        'zh,zh-CN;q=0.9',
        'Connection':
        'keep-alive',
        'Cookie':
        'JSESSIONID=DF35A0D8C08226B7872278C05ACF4048-n1; Hm_lvt_787dbcb72bb32d4789a985fd6cd53a46=1528179131,1528309476; hepUserSsoServerSSOServerTokenID=c229baebf8b349abb8a331701bfbad36; Hm_lpvt_787dbcb72bb32d4789a985fd6cd53a46=1528339496',
        'Host':
        'www.icourses.cn',
        'Referer':
        'http://www.icourses.cn/web/sword/portal/shareDetails?cId=' + str(id),
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'X-Requested-With':
        'XMLHttpRequest',
    }

    url = 'http://www.icourses.cn/web/sword/portal/shareChapter?cid=' + str(id)
    source_url = 'http://www.icourses.cn/web/sword/portal/sharerSource?cid=' + str(
        id)
    homework_url = 'http://www.icourses.cn/web/sword/portal/assignments?cid=' + str(
        id)
    exampaper_url = 'http://www.icourses.cn/web/sword/portal/testPaper?cid=' + str(
        id)
    html = requests.get(url, headers=header)
    html.encoding = html.apparent_encoding
    datasid1 = getRess1(html)
    datasid2 = getRess2(html)
    for i in range(len(datasid2)):
        if datasid2[i] not in datasid1:
            datasid1.append(datasid2[i])
    mp4_list, pdf_list = get_download_link(datasid1, id)
    mp4_num = len(mp4_list)
    pdf_num = len(pdf_list)

    source_html = requests.get(source_url, headers=header)
    source_html.encoding = source_html.apparent_encoding
    source_list = get_source_link(source_html)
    source_num = len(source_list)

    homework_html = requests.get(homework_url, headers=header)
    homework_html.encoding = homework_html.apparent_encoding
    homework_list = get_homework_and_exampaper_link(homework_html, '习题作业')
    homework_num = len(homework_list)

    exampaper_html = requests.get(exampaper_url, headers=header)
    exampaper_html.encoding = exampaper_html.apparent_encoding
    exampaper_list = get_homework_and_exampaper_link(exampaper_html, '测试试卷')
    exampaper_num = len(exampaper_list)

    print('共抓取到：视频' + str(mp4_num) + '条，pdf课件' + str(pdf_num) + '个，习题作业' +
          str(homework_num) + '个，测试试卷' + str(exampaper_num) + '个，以及其他资源' +
          str(source_num) + '条。')
    write_txt(mp4_list, pdf_list, source_list, homework_list, exampaper_list,
              loc)
    print('所有的下载链接均已写入保存地址内名为‘批量下载链接.txt’和‘分条下载链接.txt’的文本文件内！')
    change_name(mp4_list, pdf_list, source_list, homework_list, exampaper_list,
                loc)
    print('已自动生成改名文件 change_name.cmd, 双击运行即可')
    return


def getRess1(html):
    soup = BeautifulSoup(html.text, 'lxml')
    datasid = []
    for link in soup.find_all(
            'li', class_='chapter-bind-click panel noContent'):
        sec_id = link.get('data-id')
        datasid.append(sec_id)
    return datasid


def getRess2(html):
    soup = BeautifulSoup(html.text, 'lxml')
    datasid = []
    for link in soup.find_all(
            'a', class_='chapter-body-content-text section-event-t no-load'):
        sec_id = link.get('data-secid')
        datasid.append(sec_id)
    return datasid


def get_source_link(html):
    source_list = {}
    soup = BeautifulSoup(html.text, 'lxml')
    for link in soup.find_all(
            'a', class_='courseshareresources-content clearfix'):
        source_list[link.get('data-url')] = '其他资源-' + link.get('data-title')
    return source_list


def get_homework_and_exampaper_link(html, name):
    source_list = {}
    soup = BeautifulSoup(html.text, 'lxml')
    for link in soup.find_all('a', {'data-class': 'media'}):
        source_list[link.get(
            'data-url')] = str(name) + '-' + link.get('data-title')
    return source_list


def write_txt(mp4_list, pdf_list, source_list, homework_list, exampaper_list,
              loc):
    with open(loc + '\\批量下载链接.txt', 'w') as f:
        f.write('以下是视频链接：\n\n')
        write_list2(mp4_list,f)
        f.write('\n\n以下是课件下载链接：\n\n')
        write_list2(pdf_list,f)
        f.write('\n\n以下是其他资源下载链接：\n\n')
        write_list2(source_list,f)
        f.write('\n\n以下是习题作业下载链接：\n\n')
        write_list2(homework_list,f)
        f.write('\n\n以下是测试试卷下载链接：\n\n')
        write_list2(exampaper_list,f)
        f.close()
    with open(loc + '\\分条下载链接.txt', 'w') as f:
        f.write('以下是视频链接：\n\n')
        write_list1(mp4_list,f)
        f.write('\n\n以下是课件下载链接：\n\n')
        write_list1(pdf_list,f)
        f.write('\n\n以下是其他资源下载链接：\n\n')
        write_list1(source_list,f)
        f.write('\n\n以下是习题作业下载链接：\n\n')
        write_list1(homework_list,f)
        f.write('\n\n以下是测试试卷下载链接：\n\n')
        write_list1(exampaper_list,f)
        f.close()

def write_list1(write_list,f):
    for key in write_list:
        try:
            f.write(write_list[key] + ' : ' + key + '\n')
        except:
            continue
        finally:
            pass

def write_list2(write_list,f):
    for key in write_list:
        try:
            f.write(key + '\n')
        except:
            continue
        finally:
            pass

def get_id(link):
    cid = re.findall(r'[0-9]+', link)[0]
    if cid:
        return cid
    else:
        print('地址输入错误')
        return False


def get_download_link(datasid, id):
    mp4_list = {}
    pdf_list = {}
    header = {
        'Content-Type':
        'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie':
        'JSESSIONID=14D2C920A7C2D8F83C4321EDAD8AC3CF-n1; Hm_lvt_787dbcb72bb32d4789a985fd6cd53a46=1528179131,1528309476,1528342756; hepUserSsoServerSSOServerTokenID=631634c5869c4e85a8b24c273df0ccdc; Hm_lpvt_787dbcb72bb32d4789a985fd6cd53a46=1528342771',
        'Host':
        'www.icourses.cn',
        'Origin':
        'http://www.icourses.cn',
        'Referer':
        'http://www.icourses.cn/web/sword/portal/shareDetails?cId=' + str(id),
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    }
    url = 'http://www.icourses.cn/web//sword/portal/getRess'
    for i in datasid:
        payload = {'sectionId': i}
        result = requests.post(url, params=payload, headers=header)
        json = result.json()
        if len(json['model']['listRes']) != 0:
            loc = json['model']['listRes']
            for i in loc:
                if i['mediaType'] == 'mp4':
                    if 'fullResUrl' in i:
                        mp4_list[i['fullResUrl']] = i['resSortDesc'] + '-' + i['title']
                elif i['mediaType'] in ['ppt', 'pdf']:
                    if 'fullResUrl' in i:
                        pdf_list[i['fullResUrl']] = i['resSortDesc'] + '-' + i['title']
    return mp4_list, pdf_list


def change_name(mp4_list, pdf_list, source_list, homework_list, exampaper_list,
                loc):
    with open(loc + '\\change_name.cmd', 'w') as f:
        loc = loc.replace('\\', r'\\') + r'\\'
        i = 0
        name_dict = {}
        for key in mp4_list:
            name_dict[(key.split('/')[-1])] = mp4_list[key]
        for key in pdf_list:
            name_dict[(key.split('/')[-1])] = pdf_list[key]
        for key in source_list:
            name_dict[(key.split('/')[-1])] = source_list[key]
        for key in homework_list:
            name_dict[(key.split('/')[-1])] = homework_list[key]
        for key in exampaper_list:
            name_dict[(key.split('/')[-1])] = exampaper_list[key]
        for key in name_dict:
            i = i + 1
            old_name = str(key).split(r'/')[-1]
            tailor = old_name.split('.')[-1]
            new_name = str(i) + '-' + name_dict[key] + '.' + tailor
            if (r'/' in new_name):
                new_name = new_name.replace(r'/', ' ')
            try:
                f.write(r'ren "%s" "%s"&' % (old_name, new_name))
                f.write('\n')
            except:
                continue
            finally:
                pass
        f.close()


if __name__ == '__main__':
    loc = input('请输入保存地址(如 D:\爱课程下载):')
    loc = loc.replace(' ', '')
    link = input('请输入课程链接(如 http://www.icourses.cn/sCourse/course_4860.html):')
    cid = get_id(link)
    if cid:
        get_course_name(cid)
        get_html(cid, loc)
