Notas001 = input()
notas001 = int(Notas001)

print(notas001)

#100
notas100 = notas001//100
notas001 = notas001%100

#50
notas050 = notas001//50
notas001 = notas001%50

#20
notas020 = notas001//20
notas001 = notas001%20

#10
notas010 = notas001//10
notas001 = notas001%10

#5
notas005 = notas001//5
notas001 = notas001%5

#2
notas002 = notas001//2
notas001 = notas001%2

print(notas100, "nota(s) de R$ 100,00")
print(notas050, "nota(s) de R$ 50,00")
print(notas020, "nota(s) de R$ 20,00")
print(notas010, "nota(s) de R$ 10,00")
print(notas005, "nota(s) de R$ 5,00")
print(notas002, "nota(s) de R$ 2,00")
print(notas001, "nota(s) de R$ 1,00")
