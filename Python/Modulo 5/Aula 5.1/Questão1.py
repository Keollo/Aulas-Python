# -*- coding: utf-8 -*-
"""Arthur.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1E482B_ZGdwZEao4qBCzPx7-jtElVn9Zm
"""

# Entrada
def calcular_diferenca_absoluta():
    # Numeros
    primeiro_numero = float(input("Digite o primeiro número: "))
    segundo_numero = float(input("Digite o segundo número: "))

    # Processamento
    diferenca_absoluta = abs(primeiro_numero - segundo_numero)

    # Processamento
    diferenca_arredondada = round(diferenca_absoluta, 2)

    # Saida
    print(f"A diferença absoluta entre os números é: {diferenca_arredondada}")

# Chama a função
calcular_diferenca_absoluta()