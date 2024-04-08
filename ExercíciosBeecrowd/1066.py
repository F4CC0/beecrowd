v1 = int(input())
v2 = int(input())
v3 = int(input())
v4 = int(input())
v5 = int(input())

negativos = 0
positivos = 0
pares = 0

if v1<0:
    negativos = 1 + negativos
elif v1>0:
    positivos += 1
    
if v2<0:
    negativos = 1 + negativos
elif v2>0:
    positivos += 1
    
if v3<0:
    negativos = 1 + negativos
elif v3>0:
    positivos += 1

if v4<0:
    negativos = 1 + negativos
elif v4>0:
    positivos += 1

if v5<0:
    negativos = 1 + negativos
elif v5>0:
    positivos += 1
    

if v1%2==0:
    pares += 1

if v2%2==0:
    pares += 1

if v3%2==0:
    pares += 1

if v4%2==0:
    pares += 1

if v5%2==0:
    pares += 1

print(pares, "valor(es) par(es)")
print(5 - pares, "valor(es) impar(es)")
print(positivos, "valor(es) positivo(s)")
print(negativos, "valor(es) negativo(s)")

