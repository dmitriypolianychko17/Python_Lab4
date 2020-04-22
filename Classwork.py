# Funkcja apply_twice przyjmuje inną funkcję jako argument i wywołuje ją dwukrotnie wewnątrz
from itertools import accumulate, takewhile, product, permutations


def apply_twice(func, arg):
    return func(func(arg))
def add_five(x):
    return x+5
print(apply_twice(add_five, 10))

#czysta funkcja
def pure_function(x,y):
    temp = x+2*y
    return temp / (2 * x + y)

#nieczysta funkcja
some_list = []

def impure(arg):
    some_list.append(arg)

#Wyrażenia lambda
def my_func(f, arg):
    return (f(arg))
print(my_func(lambda x: 2 * x * x, 5))

#nzawana funkcja
def polynomial(x):
    return x ** 2 + 5 * x + 4
print(polynomial(-4))
print((lambda x: x ** 2 + 5 * x + 4)(-4))
double = lambda x: x*2
print(double(7))

#Funkcja map
def add_five(x):
    return x+5

nums = [11,22,33,44,55]
result = list(map(add_five,nums))
print(result)

nums = [11,22,33,44,55]
result = list(map(lambda x: x+5, nums))
print(result)

#Funkcja filter
nums = [11,22,33,44,55]
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)

#Generatory
#1
def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1
for i in countdown():
    print(i)
#2
#def infinite_sevens():
#   while True:
#        yield 7
#for i in infinite_sevens():
#    print(i)
def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i
print(list(numbers(11)))

#Dekorator
def decor(func):
    def wrap():
        print("=============")
        func()
        print("=============")
    return wrap

def print_text():
    print("Hello world!")
decorated = decor(print_text)
decorated()

@decor
def print_text2():
    print("Spam")
print_text2()

#Rekurencja
def factorial(x):
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial(5))

def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)
def is_odd(x):
    return not is_even(x)
print(is_even(23))
print(is_odd(17))

#Zbiory
num_set = {1, 2, 3, 4, 5}
world_set = (["spam", "eggs"])
print(3 in num_set)
print("spam" not in world_set)

nums = {1, 2, 1, 3, 4, 5, 1}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)

#Itertools
nums = list(accumulate(range(9)))
print(nums)
print(list(takewhile(lambda x: x <= 6, nums)))

letters = ("A", "B", "C")
print(list(product(letters, range(3))))
print(list(permutations(letters)))