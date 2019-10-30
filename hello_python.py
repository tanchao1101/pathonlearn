# def test(func22):
#     def wrapper():
#         print('开发')
#         func22()
#         print('结束')
#     return wrapper
# @test
# def test2():
#     print('test222')
# test2()
from functools import wraps


def log(name=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print('{0}.start..'.format(name))
            rest = func(*args,**kwargs)
            print('{0}.end..'.format(name))
            return rest
        return wrapper
    return decorator
@log('hellllll')
def hello():
    print('hello')
# hello()

@log('sss')
def test3(a,b):
    print(a+b)

    return a+b
# print(test3(6,5))
# print(test3.__name__)
def f(self):
    print('aaaaa:'+self.name)

def eat(cls):
    cls.eat = f
    return cls
@eat
class Cat(object):
    def __init__(self,name):
        self.name = name
cat = Cat('小黑黑')
cat.eat()