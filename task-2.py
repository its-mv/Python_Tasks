from datetime import datetime 
import time

def custom_decorator(fun):
    def wrapper(*args , **kwargs):
        a = time.time_ns()
        print(a)
        b = fun(*args , **kwargs)
        print(b)
        c = time.time_ns()
        print(c)
        return b
    return wrapper




@custom_decorator
def hello():
    print("Hello World")


hello()



# def custom_decorator(fun):
#     def wrapper(*args, **kwargs):
#         print("this are some task that should be taken care before execution")
#         result = fun(*args, **kwargs)
#         print(result)
#         print("this are some other tasks that should be executed after function completion")
#         return result
#     return wrapper

# @custom_decorator
# def sum(parv):
#     for i in range(0, parv):
#         yield (i + (i +1))
        
# a = sum(10)
# print(a)
# for i in a:
#     print(i)