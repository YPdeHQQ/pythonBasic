# _*_ coding: utf-8 _*_
# @Time: 2023/3/17 23:08
# @Author: 🎈
# @File: demo

import logging

# 简单使用
# logging.basicConfig(level=logging.DEBUG)
# logging.debug('调试中...')
# logging.info('输出的信息...')
# logging.warning('warning！')
# logging.error('出现错误！')
# logging.critical('严重错误！')
# 只输出了三条信息，这是因为日志是有一个级别的，而默认是warning级别，而比warning级别低的语句就不会输出
'''DEBUG:root:调试中...
INFO:root:输出的信息...
WARNING:root:warning！
ERROR:root:出现错误！
CRITICAL:root:严重错误！

root 是记录器名称
'''

# 输出到日志文件中
# logging.basicConfig(level=logging.INFO,
#                     filename='log.txt',
#                     filemode='w')  # 默认filemode 是追加写入的方式
# logging.debug('调试中...')
# logging.info('输出的信息...')
# logging.warning('warning！')
# logging.error('出现错误！')
# logging.critical('严重错误！')

# 美化日志输出
# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s %(levelname)s %(lineno)s >>> %(message)s',  # %()s 是固定格式
#                     datefmt='%Y-%m-%d %H:%M:%S')
# logging.info('这是一条正常信息')
# logging.warning('这是一条警告信息')
# logging.error('这是一条错误信息')
# logging.critical('这是一条致命的错误信息')


# 高级应用
# logger记录器
'''
1. 提供应用程序的调用接口
logger = logging.getLogger(__name__)  默认是root, 也可以自定义其他
2. 决定日志记录的级别
logger.setLevel()
3. 将日志内容传递到相关联的handler中
logger.addHandler() 和 logger.removeHandler()
'''

# handler处理器
'''
# 最常用的两个 StreamHandler 和 FileHandler
# 所有的Handler处理器都可以使用 setFormatter() 来设置当前Handler对象的消息格式
'''

# formatter格式器
'''
ft = logging.Formatter(fmt=None, datefmt=None, style='%')
style参数默认为%， 这表示 %(<dictionary key>)s 格式的字符串
'''


# # 记录器
# logger = logging.getLogger('redballoon')
# # print(logger)
# logger.setLevel(level=logging.DEBUG)
# # print(logger)
#
# # 处理器
# console_handler = logging.StreamHandler()
# file_handler = logging.FileHandler(filename='2023-3-18-log.txt')
#
# console_handler.setLevel(level=logging.DEBUG)
# # 如果没有给handler设置日志级别，将使用logger的日志级别
# file_handler.setLevel(level=logging.INFO)
# # * 若是设置了logger记录器的日志级别，又设置了console_handler的日志级别，则会以logger的级别为准。
#
# # 格式化器
# fmt = logging.Formatter('%(asctime)s %(levelname)s %(filename)s:%(lineno)s >>> %(message)s')
#
# # 给处理器添加格式
# console_handler.setFormatter(fmt)
# file_handler.setFormatter(fmt)
#
# # 给记录器添加处理器
# logger.addHandler(console_handler)
# logger.addHandler(file_handler)
#
# logger.debug('这是调试的信息')
# logger.info('这是一条正常信息')
# logger.warning('这是一条警告信息')
# logger.error('这是一条错误信息')
# logger.critical('这是一条致命的错误信息')


# print('=====================输出到控制台==========================')
#
# # 记录器
# logger1 = logging.getLogger('redballoon')
# logger2 = logging.getLogger('blueballoon')
# logger1.setLevel(level=logging.DEBUG)
# # logger2.setLevel(level=logging.DEBUG)
#
# # 处理器
# console_handler = logging.StreamHandler()
# console_handler.setLevel(level=logging.DEBUG)
#
# # 过滤器  满足过滤器设置的记录器名称便会被输出
# # 定义一个过滤器
# flt = logging.Filter('blueballoon')
# # 关联过滤器
# console_handler.addFilter(flt)
#
# # 格式化器
# fmt = logging.Formatter('%(name)-12s | %(asctime)s %(levelname)s %(filename)s:%(lineno)s >>> %(message)s',
#                         datefmt='%Y-%m-%d %H:%M:%S',)
#
# # 给处理器添加格式
# console_handler.setFormatter(fmt)
#
# # 给记录器添加处理器
# logger1.addHandler(console_handler)
# logger2.addHandler(console_handler)
#
# logger1.debug('这是调试的信息')
# logger1.info('这是一条正常信息')
# logger1.warning('这是一条警告信息')
# logger1.error('这是一条错误信息')
# logger1.critical('这是一条致命的错误信息')
# print('=========================================')
# logger2.debug('这是调试的信息')
# logger2.info('这是一条正常信息')
# logger2.warning('这是一条警告信息')
# logger2.error('这是一条错误信息')
# logger2.critical('这是一条致命的错误信息')




print('=====================输出到控制台==========================')

# 记录器
logger = logging.getLogger('redballoon')
logger.setLevel(level=logging.DEBUG)


# 处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(level=logging.DEBUG)

file_handler = logging.FileHandler(filename='2023-3-19-log.txt')
file_handler.setLevel(level=logging.INFO)


# 过滤器
# 定义一个过滤器
'''使用记录器的名称初始化，记录器及其子记录器将允许其事件通过筛选器。如果未指定名称，则允许每个事件'''
flt = logging.Filter()  # 通过源码可知，如果添加记录器名称则以记录器名称来过滤，未指定则可以使用Handler来过滤
# 关联过滤器
console_handler.addFilter(flt)

# 格式化器
fmt = logging.Formatter('%(name)-12s | %(asctime)s %(levelname)s %(filename)s:%(lineno)s >>> %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',)

# 给处理器添加格式
console_handler.setFormatter(fmt)
file_handler.setFormatter(fmt)

# 给记录器添加处理器
logger.addHandler(console_handler)
logger.addHandler(file_handler)


logger.debug('这是调试的信息')
logger.info('这是一条正常信息')
logger.warning('这是一条警告信息')
logger.error('这是一条错误信息')
logger.critical('这是一条致命的错误信息')
print('=========================================')
