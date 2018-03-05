import re

def getCid():
    cid = input('请输入课程链接（形式为：http://www.icourses.cn/sCourse/course_5976.html）')
    getUrl=re.findall(r'[0-9]+',str(cid))
    return getUrl[0]


if __name__ == "__main__":
    getCid()
