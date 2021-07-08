from functools import partial, wraps
import time

arr = []
isTrue = False


def wrapped(func):
    @wraps(func)
    def wrapper(args):
        print("Wrapped")
        print(args)
        func(args[0])

    @wraps(func)
    def executor(*args):
        arr.append(partial(wrapper, args))

    return executor


@wrapped
def hello(bird):
    print("Hello World " + bird)


hello("tree", "bird")
hello("crisp", "fly")
print(arr.pop(0))
time.sleep(3)
arr.pop(0)()
print(arr)

# def eventCaller(func, *args, **kwargs):
#     if(isTrue):
#         arr.append(partial(func, *args, **kwargs))
#     else:
#         func(args, kwargs)
