# coding: utf-8
import os

listing_path = '/Users/hy/Desktop/Learning_Python/python-demo/list_dirs/testing_dirs'
write_file_name = 'dirs_tree.txt'


def list_dirs_then_write_into_file(dir_name, write_file, level=1):
    if level == 1:
        print(dir_name)
        with open(write_file, 'a') as f:
            f.write(dir_name + '\r')
    lists = os.listdir(dir_name)
    # print(lists)
    for path in lists:
        # print('|    '*(level-1)+'|----'+path)
        with open(write_file, 'a') as f:
            f.write('|    '*(level-1)+'|----'+path+'\n')
        sub_path = os.path.join(dir_name, path)
        if os.path.isdir(sub_path):
            list_dirs_then_write_into_file(sub_path, write_file, level+1)


if __name__ == '__main__':
    if os.path.exists(write_file_name):
        os.remove(write_file_name)
    list_dirs_then_write_into_file(listing_path, write_file_name)
