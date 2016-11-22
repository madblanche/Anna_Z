from functools import wraps
from functools import partial

#Написать функцию-обертку для другой функции
# (без явного объявления декоратора, каррирование)
def apple():
    return 1

def wrap():
    return apple

pear = wrap()
print(pear)

#Написать декоратор для функции, который будет возвращать ссылку на оборачиваемую функцию
def wrapp(f1):
    return f1

@wrapp
def f2():
    pass

#Написать декоратор для функции без использования аргументов
def my_decorator(func):
    def wrapper():
        print('__apple__')
        func()
        print('...pear...')
    return wrapper()

@my_decorator
def fruits(kind='_fruit_'):
    print(kind)


#Разработать декоратор для функции с поддержкой аргументов (без декоратора @wraps)
def decorator_with_arguments(function_to_decorate):
    def wrapper_arguments(arg1, arg2):
        print("Here are my arguments:", arg1, arg2)
        function_to_decorate(arg1, arg2)
    return wrapper_arguments

@decorator_with_arguments
def print_animal(animal_name, animal_kind):
    print("This is animal", animal_name, animal_kind)

print_animal("Roxy", "Dog")

#Разработать декоратор для функции с поддержкой аргументов с использованием функции wraps из стандартной библиотеки functools
def mydecorator(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        print("Before decorated function")
        r = f(*args, **kwargs)
        print("After decorated function")
        return r
    return wrapped

@mydecorator
def myfunc(myarg):
    print("my function", myarg)
    return "return value"

r = myfunc('asdf')
print(r)

#Создать функцию и вызвать ее с помощью функции partial из стандартного модуля functools.
# Создать и вызвать несколько функций с разным кол-вом аргументов,
# где часть аргументов должна быть передана в partial,
# а остальная часть упущена для подальшей передаче их при вызове самой функции,
# которая получена в результате вызова функции partial
def f(a, b, c, d):
    print(a, b, c, d)

g = partial(f, 1, 2)
print(g(4, 5))
print(g(5, 6))
print(g(6, 7))

#ООП
# Создать и проинициализировать класс
class A:
    pass

A()

# Создать класс, который принимает некоторое кол-во аргументов и устанавливает их, как новые его свойства
class Student :
    def f(self, n, y):
        self.name=n
        self.year=y
        print(self.name, "is on the", self.year, "-th year")
s1=Student()
s2=Student()
s1.f("Vasya", 5)
s2.f("Petya", 6)


# Создать класс который содержит в себе public, protected и private свойства.
# Написать вызов этих свойств, если свойство вызвать нельзя, то кратко написать почему


# Создать 3 класса, где потом прописать цепочку наследования классов.
# Например A -> B -> C. Класс A является родителем для B, где B для С
g
# Создать класс A в котором определить конструктор, который должен принимать некое кол-во аргументов.
# Создать класс B, который наследуется от класса A. В классе
# B переопределить конструктор из родительского класса, где написать вызов родительского
# конструктора с модификацией аргументов (например получаем аргумент а, где в родительский конструктор передаем a + 1)


# Разработать класс с поддержкой оператора with.

