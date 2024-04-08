p = input()
q = input()
r = input()

print(p, end="#")
print(q, end="#")
print(r)

#o sep ou end deveriam separar por # as variaveis




A lógica é essa mesma.

Se a > b:

aux = a (aux salva o valor de a que é o maior pra não perder o valor quando fizer a nova atribuição)

a = b (troca do valor de a, que era maior, por b, que é menor que ele)

b = aux (b recebe o maior valor salvo na variável auxiliar)

se a > c :

aux = a (aux salva o valor de a que é o maior pra não perder o valor quando fizer a nova atribuição)

a = c (troca do valor de a, que era maior, por c, que é menor que ele)

c = aux (b recebe o maior valor salvo na variável auxiliar)

Por fim, precisa comparar B e C, porque já foi verificado a>b e a>c.

Se b > c:

aux = b (aux salva o valor de b que é o maior pra não perder o valor quando fizer a nova atribuição)

b = c (troca do valor de b, que era maior, por c, que é menor que ele)

c = aux (c recebe o maior valor salvo na variável auxiliar)

Espero que ficou entendível