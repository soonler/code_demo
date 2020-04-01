def check_iterator(obj):
    if hasattr( obj, '__iter__' ):
        if hasattr( obj, '__next__' ):
            print(f'{obj} is a iterator') # 完整迭代器协议
        else:
            print(f'{obj} is a iterable') # 可迭代对象
    else:
        print(f'{obj} can not iterable') # 不可迭代

def func1():
    yield range(5)

# check_iterator(func1)
# check_iterator(func1())

next(func1())