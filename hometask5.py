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
class Aclass:
    pass

Aclass()

# Создать класс, который принимает некоторое кол-во аргументов и устанавливает их, как новые его свойства
class Student :
    def f(self, n, y):
        self.name=n
        self.year=y
        print(self.name, "is on the", self.year, "-th year")
s1 = Student()
s2 = Student()
s1.f("Vasya", 5)
s2.f("Petya", 6)


# Создать класс который содержит в себе public, protected и private свойства.
# Написать вызов этих свойств, если свойство вызвать нельзя, то кратко написать почему
class Bclass:
    def __init__(self, name, surname, age):
        self.name = name  # public
        self._surname = surname  # protected
        self.__age = age  # private

b = Bclass('Ketty', 'Maroon', 33)
print(b.name)
print(b._surname)
#print(b.__age) If you try to call a private method,
# Python will raise a slightly misleading exception, saying that the method does not exist.
# Of course it does exist, but it's private, so it's not accessible outside the class.


# Создать 3 класса, где потом прописать цепочку наследования классов.
# Например A -> B -> C. Класс A является родителем для B, где B для С
class A:
    def __init__(self, name):
        self.name = name


class B(A):
    def __init__(self, name):
        super(B, self).__init__(name)

        self.name = '123' + name


class C(B):
    def __init__(self, name):
        super(C, self).__init__(name)
# Создать класс A в котором определить конструктор, который должен принимать некое кол-во аргументов.
# Создать класс B, который наследуется от класса A.
# В классе B переопределить конструктор из родительского класса,
# где написать вызов родительского конструктора с модификацией аргументов
# (например получаем аргумент а, где в родительский конструктор передаем a + 1)
class A1:
    def __init__(self, hours=2, seconds=10):
        self.hours = hours
        self.seconds = seconds

class B1(A1):
    def __init__(self, hours, seconds):
        super(B1, self).__init__(hours + 1, seconds + 20)

# Разработать класс с поддержкой оператора with.
class Last(object):
    def __enter__(self):
        print('sss')
        return 'sss111'
    def __exit__(self ,type, value, traceback):
        print('ok')
        return False

with Last() as s:
    print(s)

print(s)