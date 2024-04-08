a, b, c = input().split()

A = float(a)
B = float(b)
C = float(c)

#A>B>=C

if A < B:
    aux = A
    A = B
    B = aux

if C > A:
    aux = A
    A = C
    C = aux

if C > B:
    aux = B
    B = C
    C = aux

if A >= (B + C):
    print("NAO FORMA TRIANGULO")

elif A**2 == B**2 + C**2:
    print("TRIANGULO RETANGULO")

elif A**2 > B**2 + C**2:
    print("TRIANGULO OBTUSANGULO")

elif A**2 < B**2 + C**2:
    print("TRIANGULO ACUTANGULO")

if A == B and A == C and B == C:
    print ("TRIANGULO EQUILATERO")

elif A == B or A == C or B == C:
     print("TRIANGULO ISOSCELES")
