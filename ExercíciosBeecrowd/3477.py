#(3 * r**2)//2

xx, yy, zz = input().split()
x = int(xx)
y = int(yy)
z = int(zz)



if z**2 + y**2 == x**2:
    aq = (z * y)/2
    ac = (3 * (z/2)**2)/2
    print("AREA =",int(ac + aq))
else:
    print("Nao eh retangulo!")
    
