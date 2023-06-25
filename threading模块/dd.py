# _*_ coding: utf-8 _*_
# @Time: 2023/5/12 12:28
# @Author: 🎈
# @File: dd

import threading

s = 0
for i in range(101):
    s += i
    print(f'{threading.current_thread().name} --->>> {s} 【count】:【{i}】')
