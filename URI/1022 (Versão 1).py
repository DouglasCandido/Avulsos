# Python 3.8

# -*- coding: utf-8 -*-

# Essa versão do código-fonte não é aceita pelo URI, mas resolve o problema.

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

def lcm_recursive(a, b): # Faz uso do Algorítmo de Euclides para calcular o Mínimo Múltiplo Comum
    if(a == 0 or b == 0):
        return 0
    else:
        return (a * b) / gcd_recursive(a, b)

input_raw = input()

input_split = input_raw.split()

numerador_max = 0
denominador_max = 0
numerador_simplificado = 0
denominador_simplificado = 0

if(input_split.count("/") == 3):
    input_split = ''.join(input_split)
    input_split = input_split.split("/")
    for operando in input_split:
        if(input_split[0] == input_split[2] and input_split[1] == input_split[3]):
            if(input_split.index(operando) == 0):
                a = operando
                c = a
            elif(input_split.index(operando) == 1):
                b = operando
                d = b
            
        else:
            if(input_split.index(operando) == 0):
                a = operando
            elif(input_split.index(operando) == 1):
                b = operando
            elif(input_split.index(operando) == 2):
                c = operando
            elif(input_split.index(operando) == 3):
                d = operando
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    # input_calc = (a / b) / (c / d)
    numerador_max = int(a * d)
    denominador_max = int(b * c)
    mdc = gcd_recursive(numerador_max, denominador_max)
    numerador_simplificado = int(numerador_max / mdc)
    denominador_simplificado = int(denominador_max / mdc)
    output = "{numerador_max}/{denominador_max} = {numerador_simplificado}/{denominador_simplificado}"
    print(output.format(numerador_max = numerador_max, denominador_max = denominador_max, numerador_simplificado = numerador_simplificado, denominador_simplificado = denominador_simplificado))
    
    
elif(input_split.count("*") == 1):
    input_split = ''.join(input_split)
    input_split = input_split.split("*")
    for operando in input_split:
        if(input_split[0] == input_split[1]):
            conjunto_operandos = operando.split("/")
            a = conjunto_operandos[0]
            b = conjunto_operandos[1]
            c = a
            d = b
        else:
            conjunto_operandos = operando.split("/")
            if(input_split.index(operando) == 0):
                a = conjunto_operandos[0]
                b = conjunto_operandos[1]
            elif(input_split.index(operando) == 1):
                c = conjunto_operandos[0]
                d = conjunto_operandos[1]
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    # input_calc = (a / b) * (c / d)
    numerador_max = int(a * c)
    denominador_max = int(b * d)
    mdc = gcd_recursive(numerador_max, denominador_max)
    numerador_simplificado = int(numerador_max / mdc)
    denominador_simplificado = int(denominador_max / mdc)
    output = "{numerador_max}/{denominador_max} = {numerador_simplificado}/{denominador_simplificado}"
    print(output.format(numerador_max = numerador_max, denominador_max = denominador_max, numerador_simplificado = numerador_simplificado, denominador_simplificado = denominador_simplificado))
    
elif(input_split.count("+") == 1):
    input_split = ''.join(input_split)
    input_split = input_split.split("+")
    for operando in input_split:
        if(input_split[0] == input_split[1]):
            conjunto_operandos = operando.split("/")
            a = conjunto_operandos[0]
            b = conjunto_operandos[1]
            c = a
            d = b
        else:
            conjunto_operandos = operando.split("/")
            if(input_split.index(operando) == 0):
                a = conjunto_operandos[0]
                b = conjunto_operandos[1]
            elif(input_split.index(operando) == 1):
                c = conjunto_operandos[0]
                d = conjunto_operandos[1]
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    # input_calc = (a / b) + (c / d)
    denominador_max = b * d
    numerador_max = int(((denominador_max / b) * a) + ((denominador_max / d) * c))
    mdc = gcd_recursive(numerador_max, denominador_max)
    numerador_simplificado = int(numerador_max / mdc)
    denominador_simplificado = int(denominador_max / mdc)
    output = "{numerador_max}/{denominador_max} = {numerador_simplificado}/{denominador_simplificado}"
    print(output.format(numerador_max = numerador_max, denominador_max = denominador_max, numerador_simplificado = numerador_simplificado, denominador_simplificado = denominador_simplificado))
    
elif(input_split.count("-") == 1):
    input_split = ''.join(input_split)
    input_split = input_split.split("-")
    for operando in input_split:
        if(input_split[0] == input_split[1]):
            conjunto_operandos = operando.split("/")
            a = conjunto_operandos[0]
            b = conjunto_operandos[1]
            c = a
            d = b
        else:
            conjunto_operandos = operando.split("/")
            if(input_split.index(operando) == 0):
                a = conjunto_operandos[0]
                b = conjunto_operandos[1]
            elif(input_split.index(operando) == 1):
                c = conjunto_operandos[0]
                d = conjunto_operandos[1]
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    # input_calc = (a / b) - (c / d)
    denominador_max = b * d
    numerador_max = int(((denominador_max / b) * a) - ((denominador_max / d) * c))
    mdc = gcd_recursive(numerador_max, denominador_max)
    numerador_simplificado = int(numerador_max / mdc)
    denominador_simplificado = int(denominador_max / mdc)
    output = "{numerador_max}/{denominador_max} = {numerador_simplificado}/{denominador_simplificado}"
    print(output.format(numerador_max = numerador_max, denominador_max = denominador_max, numerador_simplificado = numerador_simplificado, denominador_simplificado = denominador_simplificado))






