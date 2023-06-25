# _*_ coding: utf-8 _*_
# @Time: 2023/4/10 15:37
# @Author: 🎈
# @File: demo1

import time
import threading


# 装饰器
def profile(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('COST: {}'.format(end - start))
    return wrapper


def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


@profile
def no_thread():
    fib(35)
    fib(35)


@profile
def has_thread():
    for i in range(2):
        t = threading.Thread(target=fib, args=(35,))
        t.start()
    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()


no_thread()
has_thread()
'''
['__class__', '__contains__', '__delattr__', 
'__delitem__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', 
'__getitem__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__iter__', '__le__', '__len__',
'__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__reversed__', '__setattr__', '__setitem__', 
'__sizeof__', '__str__', '__subclasshook__',
 
'clear', 'copy', 'fromkeys', 'get', 'items', 
'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
'''

'''
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError',
'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError',
'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 
'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError',
'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 
'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 
'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 
'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 
'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True',
'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError',
'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', 
'__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 

'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr',
'classmethod', 'compile', 'complex','copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 
'enumerate', 'eval', 'exec', 'exit', 'filter', 'float','format', 'frozenset', 'getattr', 'globals',
'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance','issubclass', 'iter', 'len',
'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open',
'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr',
'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
'''
