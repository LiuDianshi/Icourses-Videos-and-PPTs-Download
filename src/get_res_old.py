from bs4 import BeautifulSoup
import requests


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
                        mp4_list[i['fullResUrl']] = i['resSortDesc'] + \
                            '-' + i['title']
                elif i['mediaType'] in ['ppt', 'pdf']:
                    if 'fullResUrl' in i:
                        pdf_list[i['fullResUrl']] = i['resSortDesc'] + \
                            '-' + i['title']
    return mp4_list, pdf_list
