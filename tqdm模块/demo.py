# _*_ coding: utf-8 _*_
# @Time: 2023/5/11 14:26
# @Author: 🎈
# @File: demo

from tqdm import tqdm
import time

for i in tqdm(range(20), desc='正在下载: '):
    time.sleep(0.1)

