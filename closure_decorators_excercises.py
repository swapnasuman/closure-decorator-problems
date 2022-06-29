# Closures-Decorators Exercises

# Closure Exercise
# Using a closure, create a function, multiples_of(n) which we can use to
# create generators that generate multiples of n less than a given number.

import datetime


def multiplies_of(n):
    def multiply(k):
        # yield k * n
        for i in range(1, 10):
            mul = i * n
            if mul <= 29:
                #  print(mul)
                yield mul

    return multiply


m3 = multiplies_of(3)
m3_under30 = m3(30)
m7_under30 = multiplies_of(7)(30)

print(type(m3_under30))
print(*m3_under30)
print(*m7_under30)
'''print(type(m3_under30))
# output: <class 'generator'>

print(*m3_under30)
# output: 3 6 9 12 15 18 21 24 27

print(*m7_under30)
# output: 7 14 21 28 '''


# ----------------------------------------------------------------------

# Decorators Exercise 1
# @make_upper – make every letter of a string returned from the decorated
# function uppercase.

def uppercase(func):
    def wrapper():
        res = func()
        modified = res.upper()
        return modified

    return wrapper


def hello_world():
    return 'hello young, good day!!'


decorate = uppercase(hello_world)
print(decorate())  # output: HELLO YOUNG, GOOD DAY!!


# -----------------------------------------------------------------------

# Decorators Exercise 2
# @print_func_name – print the name of the decorated function before
# executing the function.
def message(func):
    print("my_func is running...")

    def wrapper():
        res = func()
        return res

    return wrapper


def my_func():
    print('Python is fun!!')


decorate = message(my_func)
print(decorate())
# output: my_func is running...
# Python is fun
# ----------------------------------------------------------------------

# Decorators Exercise 3
# @give_name(name) – concatenate the given name at the end of a string
# returned from the decorated function.

def printing(func):
    def wrapper():
        res = func()
        return res

    return wrapper


def greeting():
    return 'Hello'


decorate = printing(greeting)
print(decorate(), "Theresa")


# print(greeting())  # output: Hello Theresa


# ---------------------------------------------------------------------

# Decorators Exercise 4
# @print_input_type – print a data type of the input argument before
# executing the decorated function.

def decor_square(func):
    def inner():
        func()
        # result = func()
        return inner
    return decor_square


def square(n):
    print("The input data type is ", type(n))
    return n ** 2


print(square(3.5))
# output: The input data type is <class 'float'>
# 12.25
# -------------------------------------------------------------------

# Decorators Exercise 5
# @check_return_type(return_type) – check if the return type of the
# decorated function is return_type and print the result before executing
# the function.

# pass in a string


def decor_square(func):
    def inner():
        result = func()
        return result

    return decor_square


def square(n):
    print("=========Error!!")
    print("The return type is NOT ", type(str(n)))
    return n ** 2


print(square(6))
# output: =========Error!!
# The return type is NOT <class 'str'>
# 36

# pass in a float


def decor_square(func):
    def inner():
        result = func()
        return result
    return decor_square


def square(n):
    print("The return type is ", type(n))
    return n ** 2


print(square(2.9))  # output: The return type is <class 'float'>
# 8.41
# ------------------------------------------------------------------------

# Decorators Exercise 6
# @execute_log – write a function execution log on the log file. (log below)


def multiply(*nums):
    mult = 1
    for n in nums:
        mult *= n
    return mult


def hello_world():
    return 'hello world!!'


print(multiply(6, 2, 3))  # 36
print(hello_world())  # hello world!!
print(multiply(2.2, 4))  # 8.8
print(hello_world())  # hello world!!
print("function_execution.log")
print(datetime.datetime.now(), "multiply")
print(datetime.datetime.now(), "hello_world")
print(datetime.datetime.now(), "multiply")
print(datetime.datetime.now(), "hello_world")
# function_execution.log
# 2020-05-01 13:55:53.059315 multiply
# 2020-05-01 13:55:53.060312 hello_world
# 2020-05-01 13:55:53.060314 multiply
# 2020-05-01 13:55:53.060323 hello_world