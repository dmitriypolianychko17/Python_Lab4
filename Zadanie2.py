import decimal
stop = int(input("Podaj x: "))
a=stop
def float_range(start, stop, step):
    while start < stop:
        yield float(start)
        start += decimal.Decimal(step)

lista = list(float_range(0, stop, '1'))
print(lista)

result = list(map(lambda x: x*x, lista))
print(f"Result: {result}")