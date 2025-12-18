#This program helps you understand about call stack and 
# how pyhton remembers which line to rturn the execution after a function call,
# which are also called Frame Objects.

def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()
