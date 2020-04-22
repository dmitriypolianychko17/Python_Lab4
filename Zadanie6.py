n=float(input("Podaj n: "))
k=float(input("Podaj k: "))
def Newton(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return float(n) / k * Newton(n - 1, k - 1)
print(Newton(n,k))