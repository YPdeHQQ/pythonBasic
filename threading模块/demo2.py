import random, time, threading


# def thread_run(urls):
#     print(f'Current {threading.current_thread().name} is running...')
#     for url in urls:
#         print(f'{threading.current_thread().name} --->>> {url}')
#         time.sleep(random.random()*2)
#     print(f'{threading.current_thread().name} ended...')
#
#
# print(f'{threading.current_thread().name} is running...')
# t1 = threading.Thread(target=thread_run, name='T-1', args=([f'Url-{i}' for i in range(1, 11)], ))
# t2 = threading.Thread(target=thread_run, name='T-2', args=([f'Url-{i}' for i in range(11, 21)], ))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(f'{threading.current_thread().name} ended...')


def thread_run(num):
    print(f'Current {threading.current_thread().name} is running...')
    s = 0
    for i in range(num):
        s += i
        print(f'{threading.current_thread().name} --->>> {s}')
    print(f'{threading.current_thread().name} ended...')


print(f'{threading.current_thread().name} is running...')
t1 = threading.Thread(target=thread_run, name='T-1', args=(101,))
t1.start()
t1.join()

print(f'{threading.current_thread().name} ended...')
