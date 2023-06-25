# _*_ coding: utf-8 _*_
# @Time: 2023/5/12 12:43
# @Author: 🎈
# @File: 线程同步
import threading

my_lock = threading.RLock()
num = 0


class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self) -> None:
        global num
        while True:
            my_lock.acquire()
            print(f'{threading.current_thread().name} locked, Number: {num}')
            if num >= 4:
                my_lock.release()
                print(f'{threading.current_thread().name} released, Number: {num}')
                break
            num += 1
            print(f'{threading.current_thread().name} released, Number: {num}')
            my_lock.release()


if __name__ == '__main__':
    t1 = myThread('T-1')
    t2 = myThread('T-2')
    t1.start()
    t2.start()