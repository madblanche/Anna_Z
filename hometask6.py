import inspect
from http.server import (
    HTTPServer,
    BaseHTTPRequestHandler)

#Написать генерацию списка с помощью итератора
def f():
    return [i for i in range(5)]

print(f())

#Написать итератор списка с условием
def f2():
    return [(i+1)*10 for i in range(10) if i % 5 ==0]

print(f2())

#Написать генератор списка с помощью (....) и перебрать все его элементы цыклом for
def f3():
    return (
        i
        for i in range(0, 3))

for i in f3():
    print(i)

#Создать самую простую функцию-генератор (внутри функции только yield)

def f4():
    for i in range(5):
        yield i ** 2

print(f4())

#Создать функцию-генератор, которая генерирует последовательность элементов

def createGenerator():
    mylist = range(3)
    for i in mylist :
        yield i*i

mygenerator = createGenerator()

for i in mygenerator:
    print(i)

#Создать функцию-генератор для бесконечной генерации цифр
def inf():
    i = 0
    while 1:
        i += 1
        yield i

print(inf())

#Создать функцию-генератор, который может принимать значения
def coroutine(f):
    def _():
        g = f()
        if inspect.isgenerator(g):
            g.send(None)
        return g
    return _

@coroutine
def gen():
    while 1:
        print((yield))

gen().send(7)
gen().send(10)

#Написать самый простор web-server, который отдает в браузер hello world

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_header('Content-type', 'text/html')
        self.wfile.write(str('Hello, world!').encode())


def main():
    server = HTTPServer(
            ('0.0.0.0', 8000),
            MyHandler)
    server.serve_forever()

try:
    print(1)
    main()
except KeyboardInterrupt:
    print('exit')