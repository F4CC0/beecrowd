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


# -*- coding: utf-8 -*-

"""
    As cores primárias são: azul, amarela e vermelha.
    As cores secundárias são resultantes da combinação de duas cores primárias:
    verde (azul e amarela), roxa (azul e vermelha) e laranja (amarela e vermelha).
    Seu programa deverá ler 3 cores, separadas por espaços. Verificar cada cor lida.
    Se houver duas cores primárias e a cor secundária resultante da combinação
    das duas cores primárias informadas, em qualquer ordem,
    então mostrar a mensagem apropriada que relaciona as cores.
    Caso contrário, mostrar "Não há casamento adequado das cores!".
    
    ENTRADA:
    Três cores na mesma linha, separadas por espaços.
    
    SAÍDA:
    Se foram lidas azul, amarela e verde, então mostrar
    "Azul e Amarela geraram Verde!", se foram lidas azul, vermelha e roxa
    então mostrar "Azul e Vermelha geraram Roxa!",
    se foram lidas amarela, vermelha e laranja, então
    mostrar "Amarela e Vermelha geraram Laranja!".
    Caso contrário, mostrar "Não há casamento adequado das cores!".

    Exemplos de Entrada:
    
    verde azul amarela
    
    vermelha laranja amarela
    
    azul roxa verde
        
    Exemplos de Saída:
    Azul e Amarela geraram Verde!

    Amarela e Vermelha geraram Laranja!
    
    Não há casamento adequado das cores!    
    
"""

"""
    Ideia da solução:
    Ler as três cores utilizando input().split() e atribuindo as cores
    às variáveis c1, c2 e c3.
    Não queremos saber quantas cores foram informadas, mas se duas cores primárias
foram informadas e a cor secundária resultante da combinação das duas cores primárias.
    Uma solução é utilizar variáveis booleanas, Azul, Amar e Verm, uma para cada cor
    primária, para indicar se aquela cor primária foi informada ou não, e Verd,
    Roxa e Lara, para indicar se aquela cor secundária foi informada ou não.
    Inicialmente, definimos cada variável booleana como False.
    Para cada cor lida, se for encontrada a cor correspondente a uma cor,
    a variável booleana correspondente é definida como True.
    Ao final, se Azul, Amar e Verd são todas True mostrar
    "Azul e Amarela geraram Verde!", se Azul, Verm e Roxa são todas True
    mostrar "Azul e Vermelha geraram Roxa!", se Amar, Verm e Lara são todas True
    mostrar "Amarela e Vermelha geraram Laranja!".
    Caso contrário, mostrar "Não há casamento adequado das cores!".
"""

# c1, c2, c3 = Ler as 3 cores na mesma linha, separadas por espaços
c1, c2, c3 = input().split()

# Definir as variáveis lógicas para False
# Azul = False
Azul = False

# Amar = False
Amar = False

# Verm = False
Verm = False

# Verd = False
Verd = False

# Roxa = False
Roxa = False

# Lara = False
Lara = False

# se c1 == "azul" ou c2 == "azul" ou c3 == "azul"
if c1 == "azul" or c2 == "azul" or c3 == "azul":
    # então Azul = True
    Azul = True
    
# se c1 == "amarela" ou c2 == "amarela" ou c3 == "amarela"
if c1 == "amarela" or c2 == "amarela" or c3 == "amarela":
    # então Amar = True
    Amar = True
    
# se c1 == "vermelha" ou c2 == "vermelha" ou c3 == "vermelha"
if c1 == "vermelha" or c2 == "vermelha" or c3 == "vermelha":
    # então Verm = True
    Verm = True
    
# se c1 == "verde" ou c2 == "verde" ou c3 == "verde"
if c1 == "verde" or c2 == "verde" or c3 == "verde":
    # então Verd = True
    Verd = True
    
# se c1 == "roxa" ou c2 == "roxa" ou c3 == "roxa"
if c1 == "roxa" or c2 == "roxa" or c3 == "roxa":
    # então Roxa = True
    Roxa = True
    
# se c1 == "laranja" ou c2 == "laranja" ou c3 == "laranja"
if c1 == "laranja" or c2 == "laranja" or c3 == "laranja":
    # então Lara = True
    Lara = True

# se Azul e Amar e Verd são todas True
if Azul and Amar and Verd:
    # Mostrar "Azul e Amarela geraram Verde!"
    print("Azul e Amarela geraram Verde!")
# senão se Azul e Verm e Roxa são todas True
elif Azul and Verm and Roxa:
    # Mostrar "Azul e Vermelha geraram Roxa!"    
    print("Azul e Vermelha geraram Roxa!")
# senão se Amar e Verm e Lara são todas True
elif Amar and Verm and Lara:
    # Mostrar "Amarela e Vermelha geraram Laranja!"
    print("Amarela e Vermelha geraram Laranja!")
# senão mostrar "Não há casamento adequado das cores!".
else:
    print("Não há casamento adequado das cores!")