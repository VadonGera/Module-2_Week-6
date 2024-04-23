from functools import wraps

class Cache:
    def __init__(self):
        self.data = {}

    def __call__(self, func):
        self.invalidate()
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args[0] in self.data:
                return self.data[args[0]]
            result = self.data[args[0]] = func(*args, **kwargs)
            return result
        return wrapper

    def invalidate(self):
        self.data.clear()

cache = Cache()

@cache
def slow_function(arg):
    return arg

res = slow_function("первый")
res = slow_function("второй")
res = slow_function("первый")
print (len(cache.data))

class MyClass:
    @cache
    def method(self, arg):
        return arg

obj = MyClass()
res = obj.method(1)
res = obj.method(2)
res = obj.method(3)
print (len(cache.data))

@cache
async def async_func(arg):
    return arg

res = async_func("первый")
res = async_func("второй")
res = async_func("первый")
print (len(cache.data))

