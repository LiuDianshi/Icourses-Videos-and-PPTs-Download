def getLocation():
    loc = input('请输入保存位置，比如（D:\学习资料\爱课程）：')
    real_loc=''
    try:
        locSplit=str(loc).split('\\')
        for i in range(len(locSplit)):
            real_loc += locSplit[i]+'/'
    except:
        pass
    finally:
        return real_loc

if __name__ == "__main__":
    getLocation()
