# _*_ coding: utf-8 _*_
# @Time: 2023/3/16 23:10
# @Author: 🎈
# @File: demo

import os
import time

# 1. 获取当前工作的路径
print(os.getcwd())
# out:  D:\pythonProjects\pythonBasic\os模块

# 2. 指定路径为当前工作路径
# os.chdir('D:/pythonProjects')
# print(os.getcwd())
# out: D:\pythonProjects

# 3.获取所有的环境变量
# print(os.environ)

# 4.返回python运行环境的系统
print(os.name)
'''
返回值的意思
posix --> Linux 和 Mac OS
nt --> Windows
java --> Java 虚拟机环境
'''

# 5.os.mkdir 创建一个新的文件夹，不能创建多层级的文件夹
# 当文件已存在时，无法创建该文件。
# os.mkdir('test1')

# # 6.os.makedirs() 创建多级目录
# os.makedirs('cdd/dd')

# 7.os.rmdir() 删除空文件夹 如果删除的文件 如果文件夹不是空的就会报错：目录不是空的。
# os.rmdir('test')

# 8.os.removedirs() 递归删除目录
# 工作方式类似于 rmdir()，不同之处在于，如果成功删除了末尾一级目录，removedirs() 会尝试依次删除 path 中提到的每个父目录，直到抛出错误为止（但该错误会被忽略，因为这通常表示父目录不是空目录）
# os.removedirs(os.path.join('cdd', 'dd'))

# 9.删除文件
# os.remove('dd.txt')

# 10.os.rename(src, dst) 将文件或路径(文件夹)重命名,以及移动文件夹
# src 原路径，dst修改后的命名
# 只能重命名原路径 src 最后的路径或文件的名字，中间路径都必须要存在，否则就会抛出FileNotFoundError
# os.rename('test.txt', 'demo.txt')  # 重命名
# os.rename(os.path.join('test', 'test.txt'), 'test.txt')  # 移动
# os.rename('test/test.txt', 'test.txt')

# 11.os.path模块
'''os.path中的函数基本上是纯粹的字符串操作。换句话说，传入该模块函数的参数甚至不需要是一个有效路径，
该模块也不会试图访问这个路径，而仅仅是按照“路径”的通用格式对字符串进行处理'''

# 12.os.path.abspath(path) 返回路径 path 的绝对路径
print(os.path.abspath('demo.txt'))
# out: D:\pythonProjects\pythonBasic\os模块\demo.txt

# 13.os.path.exists(path) 判断该路径或文件是否存在 Bool
# print(os.path.exists('demo.txt'))
# out: True

# 14.os.path.getctime(path) 在windos下获取文件的创建时间，在Unix返回的是最后的修改时间
print(os.path.getctime('demo.txt'))
# out: 1678981495.357391
t = os.path.getctime('demo.txt')
tupTime = time.localtime(t)  # 将时间戳转换成本地时间
format_time = time.strftime("%Y-%m-%d %H:%M:%S", tupTime)  # 转换成对应的时间格式
print(format_time)  # 2023-03-16 23:46:38


# 返回path所指文件的最近访问时间（浮点型秒数）。
# print(os.path.getatime('demo.txt'))
# t = os.path.getatime('demo.txt')
# sys_time = time.localtime(t)
# formatter_time = time.strftime('%Y-%m-%d %H:%M:%S', sys_time)
# print(formatter_time)
# # out: 2023-03-17 16:04:12

# 15.os.path.getsize(path) 获取文件的大小
# print(os.path.getsize('demo.txt'))
# out: 127 (字节)

# 16.os.path.split() 将路径 path 拆分为一对，即 (head, tail)，其中，
# tail 是路径的最后一部分，而 head 里是除最后部分外的所有内容。
# tail 部分不会包含斜杠，如果 path 以斜杠结尾，则 tail 将为空。
# 如果 path 中没有斜杠，head 将为空。如果 path 为空，
# 则 head 和 tail 均为空。返回的部分是一个元组里面由两个元素
print(os.path.split(os.path.join('test', 'test.txt')))
# out: ('test', 'test.txt')
print(os.path.split('test/test2/demo3.txt'))
# out: ('test/test2', 'demo3.txt')

# a = os.path.split('D:/aa/bb')
# print(type(a))  # <class 'tuple'>
# print(a)  # ('D:/aa', 'bb')  头部和尾部
# # 当最后为’/‘时
# a = os.path.split('D:/aa/bb/')
# print(a)  # ('D:/aa/bb', '')  尾部为空
# # 当路径path中没有路径的时候
# a = os.path.split('aa')
# print(a)  # ('', 'aa')  # 头部为空
# # 当传入的路径为空时
# a = os.path.split('')
# print(a)  # ('', '')  # 头部和尾部均为空


# 17.os.path.isfile(） 判断路径是否为文件 返回布尔值
# print(os.path.isfile('demo.txt'))
# out: True

# 18.os.path.isdir() # 判断文件路径是否存在 返回布尔值
# print(os.path.isdir('test'))
# out: True

# 19.os.open()模块
'''
os.open() 打开文件的一系列操作
用法和基本的open函数很类似
注解 本函数适用于底层的 I/O。常规用途请使用内置函数 open()，该函数的 read() 和 write() 方法（及其他方法）会返回 文件对象。
要将文件描述符包装在文件对象中，请使用 fdopen()。
os.open(file, flags[, mode])
file 文件名
flags  模式
mode 可选参数， mode 设置其权限状态
'''

# 20. os.path.join()
print(os.path.join('test', 'test2', 'xxx.txt'))
# out: test\test2\xxx.txt

print(os.path.commonprefix(['C://my_file.txt', 'C://a.txt']))
print(os.path.commonpath(['http://c.biancheng.net/python/', 'http://c.biancheng.net/shell/']))


# os.path.walk(path, visit, arg) 会递归的寻找路径下所有子文件夹和文件
print(os.walk('test'))
# out: <generator object walk at 0x0000028FB505EC10>  返回的是元组的一个生成器
# (dirpath, dirnames, filenames)

# 这里设置个目录树
'''
|--test
    |--test2
        |--demo3.txt
    |--demo2.txt
'''
for path, dirname, filename in os.walk(r'D:\pythonProjects\pythonBasic\os模块\test'):
    print(path, dirname, filename)
# out: D:\pythonProjects\pythonBasic\os模块\test ['test2'] ['demo2.txt']
'''这里第一个返回结果就像在当前目录下（D:\pythonProjects\pythonBasic\os模块\test）点开之后看到的所有文件夹和文件'''
# out: D:\pythonProjects\pythonBasic\os模块\test\test2 [] ['demo3.txt']
'''第二结果就像是继续点开文件夹看看还有没有文件夹和文件，有文件夹就继续往下点开'''