import math

N, L, D = input().split()

n = int(N)
l = int(L)
d = int(D)

v = (n * d)/(1000 *  l)

print(math.ceil(v) * l)
