import requests
from bs4 import BeautifulSoup
from getcid import getCid


def getHtml():
    cid = getCid()
    paylist = {'cid': cid, 'tid': '9920d45acc1f417a87da3406f28ac6ab'}

    header = {
        'Accept':
        '*/*',
        'Accept-Encoding':
        'gzip, deflate',
        'Accept-Language':
        'zh-CN,zh;q=0.9',
        'Connection':
        'keep-alive',
        'Cookie':
        'JSESSIONID=AA3E03B7833F1E8FA62D139769C995A3-n1; Hm_lvt_787dbcb72bb32d4789a985fd6cd53a46=1520223810; hepUserSsoServerSSOServerTokenID=9571d1988b204c0d828604b47fd1e7d2; Hm_lpvt_787dbcb72bb32d4789a985fd6cd53a46=1520230752',
        'Host':
        'www.icourses.cn',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'X-Requested-With':
        'XMLHttpRequest'
    }
    initUrl = 'http://www.icourses.cn/web/sword/portal/shareChapter'
    html = requests.get(initUrl, params=paylist, headers=header)
    return html.text


if __name__ == "__main__":
    getHtml()
