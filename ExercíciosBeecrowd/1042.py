#Ler 3 valores inteiros na mesma linha.
xs, ys, zs = input().split()
x = int(xs)
y = int(ys)
z = int(zs)
#Guardar os valores originais que serão escolhidos.
b = x
n = y
m = z
#Ideia principal de como é uma ordem crescente(menor para o maior)
#x<=y<=z

if x>y:
    aux = x #aux se trata de uma variavel que apenas tem a função de guardar um valor
    x = y
    y = aux

if x>z:
    aux = x
    x = z
    z = aux

if y>z:
    aux = y
    y = z
    z = aux

print(x)#mostrar os valores já alinhados
print(y)
print(z)

print()#pular uma linha

print(b)#mostrar os valores originais de entrada
print(n)
print(m)


