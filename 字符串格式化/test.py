# _*_ coding: utf-8 _*_
# @Time: 2023/3/18 14:24
# @Author: 🎈
# @File: test


# %符 的字符串格式化
print('我的名字是 %s，今年 %d岁了。' % ('张三', 28))

# 功能符
# %[(name)][flags][width].[precision] typecode
'''
1 (name)为命名：即参数的名称，可以没有这个，怎么使用呢？注意（name需要使用括号括起来哦！！！）
# 注意：这里的name，num括号不能掉
'Hey %(name)s, there is a %(num)f number!' % {"name": name, "num": number }
2 flags可以有 +,-,' '或0。+表示右对齐。-表示左对齐。' '为一个空格，表示在正数的左侧填充一个空格，从而与负数对齐。0表示左侧使用0填充。
3 width表示显示宽度
4 precision表示小数点后精度
'''

# print('%(name)12s|' % ({'name': 'red'}))
#
# # width: 12是字符串占位的宽度
# print('%12s|' % ('redballoon'))
# # out:  redballoon|  扩充字符占位的长度
#
# # flags: (-)字符串左对齐 (+)默认，字符串右对齐 (0)对数值型操作时可以让填充为0，默认的是空格
# print('%-12s|' % ('redballoon'))
# # out:redballoon  |  左对齐
#
# print('%+12s|' % ('redballoon'))
# # out:  redballoon|  右对齐（默认）
#
# print('%012d|' % (12345))
# # out:000000012345|
#
# print('%-12.2f|' % (3.1415926))
# # out: 3.14        |


# seq = ('Google', 'Runoob', 'Taobao')
#
# # 不指定默认的键值，默认为 None
# thisdict = dict.fromkeys(seq)
# print("新字典为 : %s" % str(thisdict))
#
# # 指定默认的键值
# thisdict = dict.fromkeys(seq, 10)
# print("新字典为 : %s" % str(thisdict))

# dit = {}
# seq = ('Google', 'Runoob', 'Taobao')
# d = dit.fromkeys(seq)
# print(d)


# [{},{},{}]
k = ['name', 'age', 'gender']
v = ['mike', '19', 'man']
# z = zip(k, v)
# print(list(z))
j = list(zip(k,v))
print(j)

