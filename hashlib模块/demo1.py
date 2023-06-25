# _*_ coding: utf-8 _*_
# @Time: 2023/4/27 15:50
# @Author: 🎈
# @File: demo1


import hashlib

salt = b'redballoon123456789'
# data = 'qwer123456'
data = '''{
    "sites": [
    { "name":"菜鸟教程" , "url":"www.runoob.com" }, 
    { "name":"google" , "url":"www.google.com" }, 
    { "name":"微博" , "url":"www.weibo.com" }
    ]
}'''
# print(salt.encode('utf-8'))
# print(data.encode('utf-8'))
# print(salt)


h_md5 = hashlib.md5(salt)
h_md5.update(data.encode('utf-8'))
print('md5: ', h_md5.hexdigest())
# print(len('1f5c2fddf0828932d722db55b4074350'))


h_sha1 = hashlib.sha1(salt)
h_sha1.update(data.encode('utf-8'))
print('sha1: ', h_sha1.hexdigest())
# print(len('28461c5bd348e52e5bf229ede29eca038b86fa45'))


h_sha224 = hashlib.sha224(salt)
h_sha224.update(data.encode('utf-8'))
print('sha224: ', h_sha224.hexdigest())
# print(len('b80d0a80f4e8da90e466f182f388f6a57e92c37cd43c30621fd80bd5'))


h_sha256 = hashlib.sha256(salt)
h_sha256.update(data.encode('utf-8'))
print('sha256: ', h_sha256.hexdigest())




