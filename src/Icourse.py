import requests
from bs4 import BeautifulSoup
import re
import json
import lxml
import os


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
    html = requests.get(url, headers=header)
    html.encoding = html.apparent_encoding
    datasid = getRess(html)
    mp4_list, pdf_list = get_download_link(datasid, id)
    write_txt(mp4_list, pdf_list, loc)
    print('所有的下载链接均已写入保存地址内名为‘下载链接’的文本文件内！')
    choice = input('是否改名？(Y/N)')
    if choice in ['Y', 'y']:
        chang_name(mp4_list, pdf_list, loc)
    else:
        print('程序运行结束')
        return


def getRess(html):
    soup = BeautifulSoup(html.text, 'lxml')
    datasid = []
    for link in soup.find_all(
            'a', class_='chapter-body-content-text section-event-t no-load'):
        sec_id = link.get('data-secid')
        datasid.append(sec_id)
    return datasid


def write_txt(mp4_list, pdf_list, loc):
    with open(loc + '\\下载链接.txt', 'w') as f:
        f.write('以下是视频下载链接：')
        f.write('\n')
        for key in mp4_list:
            f.write(key)
            f.write('\n')
        f.write('\n')
        f.write('\n')
        f.write('以下是课件下载链接：')
        f.write('\n')
        for key in pdf_list:
            f.write(key)
            f.write('\n')
        f.close()


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
                    mp4_list[i['fullResUrl']] = i['title']
                elif i['mediaType'] in ['ppt', 'pdf']:
                    pdf_list[i['fullResUrl']] = i['title']
    return mp4_list, pdf_list


def chang_name(mp4_list, pdf_list, loc):
    loc = loc.replace('\\', r'\\') + r'\\'
    list = os.listdir(loc)
    name_dict = {}
    for key in mp4_list:
        name_dict[(key.split('/')[-1])] = mp4_list[key]
    for key in pdf_list:
        name_dict[(key.split('/')[-1])] = pdf_list[key]
    for item in list:
        if item in name_dict:
            old_name = loc + item
            new_name = loc + name_dict[item] + '.' + item.split('.')[-1]
            try:
                os.rename(old_name, new_name)
            except:
                continue
            finally:
                pass
        else:
            continue


if __name__ == '__main__':
    loc = input('请输入保存地址:')
    link = input('请输入课程链接:')
    cid = get_id(link)
    if cid:
        get_html(cid, loc)
