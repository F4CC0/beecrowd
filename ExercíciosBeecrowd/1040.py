n1s, n2s, n3s, n4s = input().split()
n1 = float(n1s)
n2 = float(n2s)
n3 = float(n3s)
n4 = float(n4s)

m1 = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1)/10

print("Media: {:.1f}".format(m1))
if m1 >= 7.0:
    print("Aluno aprovado.")
if m1 < 5.0:
    print("Aluno reprovado.")
if 5.0 <= m1 <= 6.9:
    print("Aluno em exame.")
    n5s = input()
    n5 = float(n5s)
    print("Nota do exame: {}".format(n5))
    m2 = (n5 + m1) / 2
    if m2 >= 5:
        print("Aluno aprovado.")
        print("Media final: {:.1f}".format(m2))
    else:
        print("Aluno reprovado", end="\n")
        print("Media final: {:.1f}".format(m2))
