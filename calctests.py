# -*- coding: utf-8 -*-
"""Calculadora.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1e8G9R1Ufv-P8CVVPC7SgCnlOTjPo46Le
"""

import unittest
from calculadora import calculadora

class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(calculadora(1, 2, '+'), 3)
        self.assertEqual(calculadora(-1, -2, '+'), -3)
        self.assertEqual(calculadora(1.5, 2.5, '+'), 4)
        self.assertIsNone(calculadora(1, 'a', '+'))  # Valor inválido
        self.assertIsNone(calculadora(1, 2, 'x'))  # Operação inválida

    def test_subtracao(self):
        self.assertEqual(calculadora(5, 3, '-'), 2)
        self.assertEqual(calculadora(-5, -3, '-'), -2)
        self.assertEqual(calculadora(5.5, 2.5, '-'), 3)
        self.assertIsNone(calculadora(1, 'a', '-'))  # Valor inválido
        self.assertIsNone(calculadora(1, 2, 'x'))  # Operação inválida

    def test_multiplicacao(self):
        self.assertEqual(calculadora(3, 4, '*'), 12)
        self.assertEqual(calculadora(-3, -4, '*'), 12)
        self.assertEqual(calculadora(1.5, 2, '*'), 3)
        self.assertIsNone(calculadora(1, 'a', '*'))  # Valor inválido
        self.assertIsNone(calculadora(1, 2, 'x'))  # Operação inválida

    def test_divisao(self):
        self.assertEqual(calculadora(10, 2, '/'), 5)
        self.assertEqual(calculadora(-10, -2, '/'), 5)
        self.assertEqual(calculadora(5, 2, '/'), 2.5)
        self.assertIsNone(calculadora(10, 0, '/'))  # Divisão por zero
        self.assertIsNone(calculadora(1, 'a', '/'))  # Valor inválido

    def test_potenciacao(self):
        self.assertEqual(calculadora(2, 3, '^'), 8)
        self.assertEqual(calculadora(-2, 3, '^'), -8)
        self.assertEqual(calculadora(2.5, 2, '^'), 6.25)
        self.assertIsNone(calculadora(1, 'a', '^'))  # Valor inválido
        self.assertIsNone(calculadora(1, 2, 'x'))  # Operação inválida

if __name__ == "__main__":
    unittest.main()
