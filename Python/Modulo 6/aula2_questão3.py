# -*- coding: utf-8 -*-
"""Aula2_Questão3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UX8SC-shQ9GZwmHkrvFmqfHcvrpm0aRQ
"""

import random

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

interseccao = list(set(lista1) & set(lista2))

print("Lista1:", lista1)
print("Lista2:", lista2)

interseccao.sort()
print("Interseccao:", interseccao)

print("Contagem")
for elemento in interseccao:
    count_lista1 = lista1.count(elemento)
    count_lista2 = lista2.count(elemento)
    print(f"{elemento}: (lista1={count_lista1}, lista2={count_lista2})")