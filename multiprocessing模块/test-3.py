# _*_ coding: utf-8 _*_
# @Time: 2023/5/12 11:14
# @Author: 🎈
# @File: test-3
from multiprocessing import Pool
import os, time, random


def run_task(name):
    print(f'Task -- {name} pid={os.getpid()} is running...')
    time.sleep(random.random()*3)
    print(f'Task {name} end.')


if __name__ == '__main__':
    print(f'Current process {os.getpid()}.')
    p = Pool()
    for i in range(10):
        p.apply_async(run_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done...')