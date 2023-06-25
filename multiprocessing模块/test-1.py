# _*_ coding: utf-8 _*_
# @Time: 2023/5/7 21:21
# @Author: 🎈
# @File: test-1
import random
import time
from multiprocessing import Process


def fun1(name):
    time.sleep(1)
    print('测试《%s》多进程' % name)


if __name__ == '__main__':
    s = time.time()
    process_list = []
    for i in range(5):  # 开启5个子进程执行fun1函数
        p = Process(target=fun1, args=(f'多进程-{i}',))  # 实例化进程对象
        p.start()
        process_list.append(p)

    for i in process_list:
        p.join()

    print('结束测试')
    e = time.time()
    print(e-s)
