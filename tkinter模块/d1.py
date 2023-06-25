from tkinter import *
from time import strftime

root = Tk()
root.geometry('500x300')

lb = Label(root, font=('微软雅黑', 32), bg='lightblue', fg='black')
lb.pack(anchor='center', fill=BOTH, expand=1)
# 定义mode标志
time = 'mode'


# 定义显示日期/时间的函数
def time_func():
    if time == 'mode':
        time1 = strftime('%H:%M:%S:%p')
    else:
        time1 = strftime('%Y-%m-%d')
    lb.config(text=time1)
    lb.after(1000, time_func)


def move_cursor(event):
    # 需要声明time为全局变量
    global time
    if time == 'mode':
        time = 'data'
    else:
        time = 'mode'


lb.bind('<Button>', move_cursor)
time_func()

root.mainloop()