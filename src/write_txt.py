# -*- coding: utf-8 -*-
"""把结果写入txt文件"""


def write(mp4_list, pdf_list, source_list, homework_list, exampaper_list,
          loc1, loc2):
    with open(loc1, 'w') as f:
        f.write('以下是视频链接：\n\n')
        write_list2(mp4_list, f)
        f.write('\n\n以下是课件下载链接：\n\n')
        write_list2(pdf_list, f)
        f.write('\n\n以下是其他资源下载链接：\n\n')
        write_list2(source_list, f)
        f.write('\n\n以下是习题作业下载链接：\n\n')
        write_list2(homework_list, f)
        f.write('\n\n以下是测试试卷下载链接：\n\n')
        write_list2(exampaper_list, f)
        f.close()
    with open(loc2, 'w') as f:
        f.write('以下是视频链接：\n\n')
        write_list1(mp4_list, f)
        f.write('\n\n以下是课件下载链接：\n\n')
        write_list1(pdf_list, f)
        f.write('\n\n以下是其他资源下载链接：\n\n')
        write_list1(source_list, f)
        f.write('\n\n以下是习题作业下载链接：\n\n')
        write_list1(homework_list, f)
        f.write('\n\n以下是测试试卷下载链接：\n\n')
        write_list1(exampaper_list, f)
        f.close()


def write_list1(write_list, f):
    for key in write_list:
        try:
            f.write(write_list[key] + ' : ' + key + '\n')
        except:
            continue
        finally:
            pass


def write_list2(write_list, f):
    for key in write_list:
        try:
            f.write(key + '\n')
        except:
            continue
        finally:
            pass


def write_txt(mp4_list, pdf_list, source_list, homework_list, exampaper_list, loc, mode):
    if(mode == 0):
        write(mp4_list, pdf_list, source_list, homework_list,
              exampaper_list, loc + '\\批量下载链接.txt', loc + '\\分条下载链接.txt')
    if(mode == 1):
        write(mp4_list, pdf_list, source_list, homework_list,
              exampaper_list, loc + '/批量下载链接.txt', loc + '/分条下载链接.txt')
