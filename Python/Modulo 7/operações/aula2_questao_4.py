# -*- coding: utf-8 -*-
"""aula2_questao 4

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_KVQxZ5Im-hP1zM04LaK1GAWoLwW4JPZ
"""

import re

def validador_senha(senha):
    # Pelo menos 8 caracteres de comprimento
    if len(senha) < 8:
        return False

    # Contém pelo menos uma letra maiúscula
    if not re.search(r'[A-Z]', senha):
        return False

    # Contém pelo menos uma letra minúscula
    if not re.search(r'[a-z]', senha):
        return False

    # Contém pelo menos um número
    if not re.search(r'\d', senha):
        return False

    # Contém pelo menos um caractere especial
    if not re.search(r'[@#$%^&+=]', senha):
        return False

    # Se passou por todas as verificações, a senha é válida
    return True

# Solicitar senha ao usuário
senha_digitada = input("Digite uma senha para validar: ")

# Verificar se a senha atende aos critérios
if validador_senha(senha_digitada):
    print("A senha é válida.")
else:
    print("A senha não atende aos critérios necessários.")