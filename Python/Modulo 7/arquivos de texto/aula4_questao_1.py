# -*- coding: utf-8 -*-
"""aula4_questao 1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_KVQxZ5Im-hP1zM04LaK1GAWoLwW4JPZ
"""

def salvar_frase_arquivo():
    # Solicitar uma frase ao usuário
    frase = input("Digite uma frase: ")

    # Caminho do arquivo onde vamos salvar a frase
    nome_arquivo = "frase.txt"

    # Tentar abrir o arquivo para escrita
    try:
        with open(nome_arquivo, 'w') as arquivo:
            # Escrever a frase no arquivo
            arquivo.write(frase)

        # Obter o caminho completo do arquivo
        import os
        caminho_completo = os.path.abspath(nome_arquivo)

        # Imprimir o caminho completo do arquivo salvo
        print(f"Frase salva em {caminho_completo}")

    except IOError:
        print(f"Erro ao tentar abrir o arquivo {nome_arquivo} para escrita")

# Chamada da função para salvar a frase
salvar_frase_arquivo()