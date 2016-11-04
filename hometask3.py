"""
hometask #3
"""
# create list, tuple, dictionary, set by 2 methods
l1 = list()
l2 = []
t1 = tuple()
t2 = ()
d1 = dict()
d2 = {}
s1 = set()
s2 = {'a', 'b'}
# create list with repeated elements, get list with unique elements
l3 = [1, 2, 3, 1, 3, 4, 5, 5, 4, 5, 6]
l4 = list(set(l3))
# create dictionary, get list of keys from this dictionary
d3 = {'apple': 1, 'kiwi': 2, 'banana': 3}
l5 = list(d3.keys())
# create an empty function, show its result of execution in console
def func_1():
    pass
f1 = func_1()
print(f1)
# create function that returns a number
def func_2():
    return 1
# create function with arguments: first required and second standard value
def func_3(a, b=5):
    return a + b
f3 = func_3(1)
print(f3)
# create function with undefined set of arguments (*args)
def func_4(*args):
    return args
f4 = func_4(1, 2, 3)
print(f4)
# create function with key arguments (**kwargs)
def func_5(**kwargs):
    return kwargs
f5 = func_5(a=1, b=2, c=3)
print(f5)
# create function with key and standard arguments
def func_6(d, **kwargs):
    return d, kwargs
f6 = func_6(d=6, a=1, b=2, c=3)
print(f6)
# create function with one required, by demand(standard value) argument,
# set of arguments and key arguments where at least one key argument should
# have standard value
def func_7(k, l=2, *args, **kwargs):
    return k, l, args, kwargs
f7 = func_7(7,2,3,4,m=5,n=6)
print(f7)
# create function with access to global variable
X = 88
def func_8():
    global X
    X = 99
func_8()
print(X)
# create function with access to nonlocal variable
x = 0
def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
        print("inner:", x)
    inner()
    print("outer:", x)
outer()
print("global:", x)
# create function with list, function adds some arguments to list
def func_9(*args):
    list_1 =args + (2,2,2,2)
    return list_1
f9 =func_9(3,3)
print(f9)