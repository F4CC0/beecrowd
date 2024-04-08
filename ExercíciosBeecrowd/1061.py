lixo1, dia1 = input().split()
h1, m1, s1 = input().split(" : ")
lixo2, dia2 = input().split()
h2, m2, s2 = input().split(" : ")

h1i, h2i, m1i, m2i, s1i, s2i = int(h1), int(h2), int(m1), int(m2), int(s1), int(s2)
dia1i, dia2i = int(dia1), int(dia2)

sf, mf, hf, df = 0, 0, 0, 0

sf = s2i - s1i
mf = m2i - m1i
hf = h2i - h1i
df = dia2i - dia1i

if sf < 0:
    sf += 60
    mf -= 1

if mf < 0:
    mf += 60
    hf -= 1

if hf < 0:
    hf += 24
    df -= 1

print("{} dia(s)".format(df))
print("{} hora(s)".format(hf))
print("{} minuto(s)".format(mf))
print("{} segundo(s)".format(sf))
