# a = {'a', 'b', 'c', 'd', 'e'}
# b = {'a', 'b', 'c', 'f', 'g'}
#
# print(a-b)  # 在a中存在，b中不存在


# a = set('abracadabra')
# b = set('alacazam')
# print(a)
# print(b)
#
# print(a-b)
# print(b-a)

# print(a | b)  # 并集
#
# print(a & b)  # 交集
#
# print(a ^ b)  # 相当于交集的补集


# a = [('mark', ''), ('kk', ''), ('derk', '')]
# print(dict(a))
# import sys
#
# print('命令行参数如下:')
# for i in sys.argv:
#     print(i)
# print('\n\nPython 路径为：', sys.path, '\n')


# import json

# a = {'name': '小王', 'age': 18, 'gender': True, 'grade': None, 'skills': ['javascript', 'java', 'css', 'python', 'c++']}
# with open('t.json', mode='r', encoding='utf-8') as f:
#     # 将字典转为str写入json文件
#     # json.dump(a, f, ensure_ascii=False)
#     # 将文件中的json数据读取出来
#     data = json.load(f)
# print(type(data))

# print(ord('A'))  # => 65
# print(chr(65))  # => A

# list1 = [1,2,3,4]
# print(id(list1))
# list2 = list1.copy()
# print(id(list2))
# list1.append(5)
# print(id(list1))

# s = 'hello world'
# s1 = list(s)
# s2 = ''.join(s1)
# print(id(s))
# print(id(s1))
# print(id(s2))
# print(s2)


# ss0 = 'hi'
# ss1 = 'h' + 'i'
# ss2 = ''.join(ss0)
# print(id(ss0))
# print(id(ss1))
# print(id(ss2))
# print(ss0 == ss1 == ss2)
# print(id(ss0) == id(ss1))
# print(id(ss0) == id(ss2))


# s = 'hello world'
# s1 = s + ''
# print(id(s))
# print(id(s1))

# s9 = "Python猫是来⾃喵星的客⼈，它喜欢地球和⼈类，正在学习Python，⽽且想借助Python变成⼈，它的微信公众号也叫Python猫，欢迎你关注哦，喵喵喵喵~~~"
# s0 = "Python猫是来⾃喵星的客⼈，它喜欢地球和⼈类，正在学习Python，⽽且想借助Python变成⼈，它的微信公众号也叫Python猫，欢迎你关注哦，喵喵喵喵~~~"
# print(s9 == s0)
# print(id(s9) == id(s0))
# print(hash(s9) == hash(s0))
# print(id(s9))
# print(id(s0))


# import sys
# print(sys.version_info)
# print(sys.version)

# print('我是谁'.encode('utf-8'))
# b'\xe6\x88\x91\xe6\x98\xaf\xe8\xb0\x81'

# print('我是谁'.encode('gbk'))
# b'\xce\xd2\xca\xc7\xcb\xad'


# def to_str(byte_str):
#     if isinstance(byte_str, bytes):
#         value = byte_str.decode('utf-8')
#     else:
#         value = byte_str
#     return value


# print(repr('hello'))
# print(False or 'NULL')
# print(int(False or 'null'))
# print(int(True))
#
# a = [1,2,3,4,5,6]
# b = a[:]
# print(id(a))
# print(id(b))


# import logging
#
# logging.basicConfig(level=logging.DEBUG,
#                     filename='info_log.txt',
#                     format='%(asctime)s %(levelname)s %(filename)s:%(lineno)s >>> %(message)s',  # %()s 是固定格式
#                     datefmt='%Y-%m-%d %H:%M:%S')
#
#
# def get_info(num):
#     logging.debug(f'这是第{num}条数据')
#
#
# for i in range(100):
#     get_info(i)


"""检验ip是否可用"""
# import requests
#
# IP = '38.7.207.92'
# PORT = '80'
#
#
# def proxy(ip, port):
#     url = 'http://www.httpbin.org/get'
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
#     }
#     proxies = {
#         'http': f'{ip}:{port}',
#         'https': f'{ip}:{port}',
#     }
#     response = requests.get(url, headers=headers, proxies=proxies, timeout=(5, 10))
#     print(response.text)
#     data = response.json()
#     if data['origin'] == ip:
#         print(f'{ip}>>>可用')
#     else:
#         print(f'{ip}>>>不可用！！！')
#
#
# proxy(IP, PORT)

# from urllib.request import ProxyHandler, build_opener
#
# url = 'http://www.httpbin.org/get'
#
# proxies = '58.246.58.150:9002'
# proxy = ProxyHandler({
#     'http': f'http://{proxies}',
#     'https': f'https://{proxies}',
# })
# opener = build_opener(proxy)
# try:
#     response = opener.open(url)
#     print(response.read().decode('utf-8'))
# except:
#     pass


# l = [13, 14, 25, 43, 45, 6, 7, 54]
# print('reverse 之前:', l)
# l.reverse()
# print('reverse 之后:', l)


# liss = [13, 14, 25, 43, 45, 6, 7, 54]
# print(liss)
# lists = [i for i in reversed(liss)]
# print(liss)
# print(lists)


# 可变序列类型的浅拷贝copy
# s = [1, 2, 3, 4, 5, 6]
# print(id(s))
# ss = s.copy()
# print(id(ss))
# print(s is ss)

# s = [1, 2, 3, 4, 5, 6]
# print(id(s))
# print(s)
# ss = s[:]
# ss[0] = 9
# print(id(ss))
# print(ss)
# print(s is ss)


# help(chr)
# print(ord('A'))
# print(chr(65))

# 输入ascii字符并转化为十进制数进行排序
# ascii_n = ['A', 'B', 'C', 'a', 'b', 'c']
#
#
# def fun_ascii_reversed(iterable: list, reverse=None) -> list:
#     l = []
#     for i in iterable:
#         n = ord(i)
#         l.append(n)
#     if reverse:
#         l.reverse()
#         return l
#     return l
#
#
# s = fun_ascii_reversed(ascii_n)
# print(s)

# s = "They'Re Bill'S Friends From The Uk"
# print(s.capitalize())  # They're bill's friends from the uk
# print(s.title())  # They'Re Bill'S Friends From The Uk

# print({c for c in 'abracadabra' if c not in 'abc'})


# import os

# path, file_name = os.path.split('E:\pythonProjects\pythonBasic\info_log.txt')
# # ('E:\\pythonProjects\\pythonBasic', 'info_log.txt')
# print(path, file_name)

# t = (1, 2, 3, 4, 5, 6)
# s = tuple(reversed(t))
# print(s)

# s = 'bicycle'
# print(id(s))
# s1 = s[::-1]
# print(id(s1))

# board = [['_'] * 3 for i in range(3)]
# print(board)


# import math
# PI = math.pi
# print(PI)

# for i in range(10):
#     PI += 1
#     with open('pi_digits.txt', mode='a')as file_object:
#         contents = file_object.write(str(PI)+'\n')
#         print(contents)


# 读取文件所有内容
with open('pi_digits.txt', mode='r')as file_object:
    contents = file_object.read().rstrip()  # rstrip() 去除文件末尾读取的空行
    print(contents)
















