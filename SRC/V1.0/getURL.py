from bs4 import BeautifulSoup
import lxml
import re
from getHtml import getHtml

def getURL():
    result = getHtml()
    soup = BeautifulSoup(result)

    file = []
    title = []
    for link in soup.find_all('a'):
        target = link.get('data-url')
        gettitle = link.get('data-title')
        if gettitle:
            if (str(gettitle) not in ['教材内容', '评价考核', '教学设计', '重点难点']):
                title.append(gettitle)
        a = re.findall(r'//office', str(target))
        if not a:
            if target:
                file.append(target)
    return title,file


if __name__ == "__main__":
    getURL()