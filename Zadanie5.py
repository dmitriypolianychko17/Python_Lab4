from math import *
x = float(input("Podaj x: "))
def decor(func):
    def wrap():
        print("Rownanie: y=(sin(x)+tg(x))/2")
        func()
        print("==================")
    return wrap

def print_text():
    print(f"Result: {(sin(x)+tan(x))/2}")
decorated = decor(print_text)
decorated()