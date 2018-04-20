import requests
from bs4 import BeautifulSoup
import re
import lxml
import os

header = {
    'Cookie':
    'JSESSIONID=AA3E03B7833F1E8FA62D139769C995A3-n1; Hm_lvt_787dbcb72bb32d4789a985fd6cd53a46=1520223810; hepUserSsoServerSSOServerTokenID=9571d1988b204c0d828604b47fd1e7d2; Hm_lpvt_787dbcb72bb32d4789a985fd6cd53a46=1520230752',
    'Host':
    'www.icourses.cn',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
}


def get_html(id, loc):
    url = 'http://www.icourses.cn/web/sword/portal/shareChapter?cid=' + \
        str(id)+'& tid=f239fb9342df4dce876d855d231eeff3'
    html = requests.get(url, headers=header)
    html.encoding = html.apparent_encoding
    mp4_list, pdf_list = get_download_link(html.text)
    write_txt(mp4_list, pdf_list, loc)
    print('所有的下载链接均已写入保存地址内名为‘下载链接’的文本文件内！')
    choice = input('是否改名？(Y/N)')
    if choice in ['Y', 'y']:
        chang_name(mp4_list, pdf_list, loc)
    else:
        print('程序运行结束')
        return


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


def get_download_link(html):
    soup = BeautifulSoup(html, 'lxml')
    pdf_list = {}
    mp4_list = {}
    for link in soup.find_all('a'):
        if link.get('data-type'):
            file_type = link.get('data-type')
            if file_type == 'mp4':
                mp4_list[link.get('data-url')] = link.get('data-title')
            elif (file_type in [
                    'ppt', 'pdf'
            ]) and (link.get('data-url').split('.')[-1] == 'pdf'):
                pdf_list[link.get('data-url')] = link.get('data-title')
            else:
                continue
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
            os.rename(old_name, new_name)
        else:
            continue


if __name__ == '__main__':
    loc = input('请输入保存地址:')
    link = input('请输入课程链接:')
    cid = get_id(link)
    if cid:
        get_html(cid, loc)
