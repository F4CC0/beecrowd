# -*- coding: utf-8 -*-
a1, b1, c1 = input().split()
a = int(a1)
b = int(b1)
c = int(c1)

maiorAB = ((a + b) + abs(a-b))/2
maiorAC = ((a + c) + abs(a-c))/2
maior = ((maiorAB + maiorAC) + abs(maiorAB-maiorAC))/2

print(int(maior), "eh o maior")

