# _*_ coding: utf-8 _*_
# @Time: 2023/5/7 21:28
# @Author: 🎈
# @File: test-2
from multiprocessing import Process, Pool
import os, time, random


def fun1(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)  # 随机一个运行等待时间
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))  # 执行该任务耗时


if __name__ == '__main__':
    s = time.time()
    pool = Pool()  # 创建一个5个进程的进程池

    for i in range(10):
        pool.apply_async(func=fun1, args=(i,))

    pool.close()
    pool.join()
    print('结束测试')
    e = time.time()
    print('Task co-time:', e-s)
