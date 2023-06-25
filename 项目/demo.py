# _*_ coding: utf-8 _*_
# @Time: 2023/5/18 21:53
# @Author: 🎈
# @File: demo

import os
import datetime
import logging

logging.basicConfig(level=logging.INFO,
                    filename='SpiderLog.txt',
                    filemode='a',
                    format='%(asctime)s %(levelname)s %(filename)s:%(lineno)s >>> %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

date = datetime.datetime.now()
y = date.year
m = date.month
d = date.day

dd = [f'{y}-{m}-{i}' for i in range(d, d+6)]

for index, name in enumerate(dd.copy()):
    folder_path = name
    logging.info('创建文件夹: %s', name)
    if not os.path.exists(name):
        os.mkdir(name)
    dd.pop(0)

    # os.path.exists(folder_path) or os.mkdir(folder_path)
    # dd.remove(i)

print(dd)


