idade_dias = int(input())

anos = int(idade_dias/365)

resto = idade_dias - anos * 365

meses = int(resto/30)

dias = resto - meses * 30

print(anos, "ano(s)")
print(meses, "mes(es)")
print(dias, "dia(s)")

