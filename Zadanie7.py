A = {0, 1, 2, 3}
B = {2, 3, 4, 5}
print("Suma: ", A.union(B))
print("Część wspólna: ", A.intersection(B))
print("Różnica A-B: ", A.difference(B))
print("Różnica B-A: ", B.difference(A))
print("Różnica symetryczna: ", A.symmetric_difference(B))
print("Czy zbiór B jest podzbiorem zbioru A: ", B.issubset(A))
print("Usuwanie elementu 0 ze zbioru A: ", A.discard(0))
print("Usuwanie i zwracanie pierwszego elementu zbioru A: ", A.pop())








