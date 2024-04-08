aa, bb, cc, dd, ee = input().split()

a = int(aa)
b = int(bb)
c = int(cc)
d = int(dd)
e = int(ee)

quant = 0

if a %5 == 0:
    quant += 1

if b %5 == 0:
    quant += 1

if c %5 == 0:
    quant += 1

if d %5 == 0:
    quant += 1

if e %5 == 0:
    quant += 1

print("A quantidade de valores lidos multiplos de 5 é:",quant)




