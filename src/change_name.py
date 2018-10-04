def change_name_windows(name_dict, loc):
    with open(loc + '\\change_name.cmd', 'w') as f:
        loc = loc.replace('\\', r'\\') + r'\\'
        i = 0
        for key in name_dict:
            i = i+1
            old_name = str(key).split(r'/')[-1]
            tailor = old_name.split('.')[-1]
            new_name = str(i) + '-' + name_dict[key] + '.' + tailor
            if(r'/' in new_name):
                new_name = new_name.replace(r'/', ' ')
            try:
                f.write(r'ren "%s" "%s"&' % (old_name, new_name))
                f.write('\n')
            except:
                continue
            finally:
                pass
        f.close()


def change_name_linux(name_dict, loc):
    with open(loc + '/change_name.sh', 'w') as f:
        i = 0
        for key in name_dict:
            i = i+1
            old_name = str(key).split(r'/')[-1]
            tailor = old_name.split('.')[-1]
            new_name = str(i) + '-' + name_dict[key] + '.' + tailor
            if(r'/' in new_name):
                new_name = new_name.replace(r'/', ' ')
            try:
                f.write(r'mv "%s" "%s"' % (old_name, new_name))
                f.write('\n')
            except:
                continue
            finally:
                pass
        f.close()


def get_name_dict(mp4_list, pdf_list, source_list, homework_list, exampaper_list):
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
    return name_dict


def change_name(mp4_list, pdf_list, source_list, homework_list, exampaper_list, loc, mode):
    name_dict = get_name_dict(
        mp4_list, pdf_list, source_list, homework_list, exampaper_list)
    if(mode == 0):
        change_name_windows(name_dict, loc)
    if(mode == 1):
        change_name_linux(name_dict, loc)
