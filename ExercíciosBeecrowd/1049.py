# -*- coding: utf-8 -*-
#Ler 3 valores
a = input()
b = input()
c = input()
#Criar condiçoes para cada escolha possivel digitada do usuario
if a == "vertebrado" and b == "ave" and c == "carnivoro":
    print("aguia")
elif a == "vertebrado" and b == "ave" and c == "onivoro":
    print("pomba")
elif a == "vertebrado" and b == "mamifero" and c == "onivoro":
    print("homem")
elif a == "vertebrado" and b == "mamifero" and c == "herbivoro":
    print("vaca")
elif a == "invertebrado" and b == "inseto" and c == "hematofago":
    print("pulga")
elif a == "invertebrado" and b == "inseto" and c == "herbivoro":
    print("lagarta")
elif a == "invertebrado" and b == "anelideo" and c == "hematofago":
    print("sanguessuga")
elif a == "invertebrado" and b == "anelideo" and c == "onivoro":
    print("minhoca")
