# Python 3.8

# -*- coding: utf-8 -*-

# Essa versão do código-fonte é aceita pelo URI.

# By DouglasCandido

'''
1022 - TDA Racional
https://www.urionlinejudge.com.br/judge/pt/problems/view/1022
'''

def gcd_recursive(a, b): # Algorítmo de Euclides para calcular o Máximo Divisor Comum
    if(b == 0):
        return a
    else:
        return gcd_recursive(b, a % b)

n1 = 0
d1 = 0
n2 = 0
d2 = 0
numerador_max = 0
denominador_max = 0
mdc = 0
numerador_simplificado = 0
denominador_simplificado = 0

op = ''

aux = int(input())

while aux > 0:

    n1, c1, d1, op, n2, c3, d2 = map(str, input().split())

    n1 = int(n1)
    d1 = int(d1)
    n2 = int(n2)
    d2 = int(d2)

    if op == '+':
        numerador_max = (n1 * d2 + n2 * d1) 
        denominador_max = d1 * d2

    elif op == '-':
        numerador_max = (n1 * d2 - n2 * d1) 
        denominador_max = d1 * d2

    elif op == '*':
        numerador_max = n1 * n2
        denominador_max = d1 * d2

    elif op == '/':
        numerador_max = n1 * d2
        denominador_max = n2 * d1

    mdc = gcd_recursive(numerador_max, denominador_max)

    if mdc == 0:
        numerador_simplificado = numerador_max
        denominador_simplificado = denominador_max
    else:
        numerador_simplificado = int(numerador_max / mdc)
        denominador_simplificado = int(denominador_max / mdc)

    output = "{numerador_max}/{denominador_max} = {numerador_simplificado}/{denominador_simplificado}"
    print(output.format(numerador_max = numerador_max, denominador_max = denominador_max, numerador_simplificado = numerador_simplificado, denominador_simplificado = denominador_simplificado))

    aux = aux - 1