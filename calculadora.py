# -*- coding: utf-8 -*-
"""Calculadora.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1e8G9R1Ufv-P8CVVPC7SgCnlOTjPo46Le
"""

def calculadora(valor1, valor2, operacao):
    # Verifica se os valores de entrada são números:
    try:
        valor1 = float(valor1)
        valor2 = float(valor2)
    except ValueError:
        print("Erro: apenas números podem ser inseridos na operação.")
        return None

    # Verifica a operação solicitada
    if operacao == '+':
        return valor1 + valor2
    elif operacao == '-':
        return valor1 - valor2
    elif operacao == '*':
        return valor1 * valor2
    elif operacao == '/':
        if valor2 == 0:
            print("Erro: não é possível dividir por zero.")
            return None
        return valor1 / valor2
    elif operacao == '^':
        return valor1 ** valor2
    else:
        print("Erro: operação inválida.")
        return None


# Testando a calculadora
# Exemplos de entrada
valor1 = input("Primeiro número: ")
valor2 = input("Segundo número: ")
operacao = input("Operação (+, -, *, /, ^): ")

resultado = calculadora(valor1, valor2, operacao)

if resultado is not None:
    print(f"Resultado: {resultado}")