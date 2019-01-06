# -*- coding: utf-8 -*-
"""新的解析方式，解析PPT课件"""

import requests
import json


def get_res_link_new(cid):
    mp4_list = {}
    pdf_list = {}
    url = 'http://mobile.icourses.cn/hep-mobile/sword/app/share/detail/getCharacters'
    data = {
        'subjectType': 1,
        'courseId': cid
    }
    try:
        html = requests.post(url, params=data, timeout=40)
    except:
        return mp4_list, pdf_list
    finally:
        pass
    html_json = html.json()
    length_chap = len(html_json['data'])
    for i in range(0, length_chap):
        chapter = html_json['data'][i]
        if len(chapter['childList']) > 0:
            length_class = len(html_json['data'][i]['childList'])
            for j in range(0, length_class):
                res = html_json['data'][i]['childList'][j]['resList']
                for k in res:
                    try:
                        if k.get('fullResUrl'):
                            if k.get('mediaType') == 'mp4':
                                mp4_list[k.get('fullResUrl')] = str(
                                    i) + '-' + str(j) + k.get('title')
                            if k.get('mediaType') in ['pdf', 'ppt']:
                                pdf_list[k.get('fullResUrl')] = str(
                                    i) + '-' + str(j) + k.get('title')
                    except:
                        continue
                    finally:
                        pass
        else:
            res = html_json['data'][i]['resList']
            for k in res:
                try:
                    print(k.get('title'))
                    if k.get('fullResUrl'):
                        if k.get('mediaType') == 'mp4':
                            mp4_list[k.get('fullResUrl')] = str(
                                i) + '-' + str(j) + k.get('title')
                        if k.get('mediaType') in ['pdf', 'ppt']:
                            pdf_list[k.get('fullResUrl')] = str(
                                i) + '-' + str(j) + k.get('title')
                except:
                    continue
                finally:
                    pass
    return mp4_list, pdf_list
