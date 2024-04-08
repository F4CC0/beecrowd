"""
Primeiramente, eu li um valor em uma linha e depois eu li 5 valores na mesma linha,
em seguida eu criei uma variavel que vai armazenar uma informacao, se ela for verdadeira, é somado 1 a sua variavel, se ela for falsa, ela permanece com o mesmo valor original,
depois eu criei as condicionais para cada variavel (a, b, c, d, e) para que, se elas forem iguais a primeira variavel lida (t), que seria a resposta certa, a condição soma 1 valor na minha variavel de armazenamento (cont)
depois de todas as condicionais, eu apenas mostrei o valor da minha variavel que armazenou as respostas certas (cont).
"""

#Ler um valor e em seguida transforma lo em inteiro.

T = input() 
t = int(T)

#Ler cinco valores na mesma linha.

aa, bb, cc, dd, ee = input().split()

#Transformar os cinco valores em inteiros.

a = int(aa)
b = int(bb)
c = int(cc)
d = int(dd)
e = int(ee)

#Variavel que vai armazenar a quantidade de respostas certas.

cont = 0

#Condicionais para cada variavel (a, b, c, d, e), que se forem iguais a primeira variavel lida (t), e somado 1 a variavel de armazenamento de resposta certa (cont).
if a == t:
    cont += 1
if b == t:
    cont += 1
if c == t:
    cont += 1
if d == t:
    cont += 1
if e == t:
    cont += 1

#Mostrar o valor dentro da variavel cont.

print(cont)
