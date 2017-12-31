# coding: utf-8
import os
import json

# A terrific website for parsing json files.
# https://www.json.cn


# If running on Windows, you can use the relative path.
listing_path = '/Users/hy/Downloads'
write_file_name = 'dirs_tree.txt'
check_json_result = 'json_check.txt'


def list_dirs_tree_and_check_json_files(dir_name, write_file, check_json, level=1):
    if level == 1:
        print(dir_name)
        with open(write_file, 'a') as f:
            f.write(dir_name + '\r')
    lists = os.listdir(dir_name)
    # print(lists)
    for path in lists:
        print('|    '*(level-1)+'|----'+path)
        with open(write_file, 'a') as f:
            f.write('|    '*(level-1)+'|----'+path+'\n')
        next_path = os.path.join(dir_name, path)
        if os.path.isdir(next_path):
            list_dirs_tree_and_check_json_files(next_path, write_file, level+1)
        else:
            if os.path.splitext(next_path) == '.json':
                print('This is a json file: ', next_path)
                try:
                    with open(next_path, 'r', encoding='utf-8') as f:
                        json.load(f)
                except UnicodeDecodeError as e:
                    print("UnicodeDecodeError: ", e)
                    try:
                        with open(next_path, 'r', encoding='gbk') as f:
                            json.load(f)
                            print('GBK decode successfully.')
                    except ValueError as e:
                        print('Error with this json: ', next_path)
                        print('ValueError: ', e)
                        with open(check_json, 'a') as f:
                            f.write('Error with this json: '+next_path+'\n')
                            f.write('ValueError: '+str(e)+'\n\n')
                except ValueError as e:
                    print('Error with this json: ', next_path)
                    print('ValueError: ', e)
                    with open(check_json, 'a') as f:
                        f.write('Error with this json: ' + next_path + '\n')
                        f.write('ValueError: ' + str(e) + '\n\n')
                else:
                    print('No Error. Bravo!')
            else:
                pass
                # print('Not a json file.')


if __name__ == '__main__':
    # list_dirs_then_print(listing_path)
    if os.path.exists(write_file_name):
        os.remove(write_file_name)
    if os.path.exists(check_json_result):
        os.remove(check_json_result)
    list_dirs_tree_and_check_json_files(listing_path, write_file_name, check_json_result)
