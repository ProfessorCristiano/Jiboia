'''
   Nome: jiboia.py
   Autor: Cristiano Teixeira
   Função: Biblioteca traduzir instruções em português estruturado 
   para instruções em Python, com objetivo de ser aplicado como alternativa 
   para aulas de lógica de programação para crianças e iniciantes.
   Versão: 2.1
   Data: 09/09/25 Atualização: 10/09/ 

   Para executar deixe o arquivo jyboia.py na mesma pasta do seu projeto 
   e adcione a linha abaixo no seu script:
   from jiboia import *

'''

import inspect

def escreva(*args):
    print(*args)

def pulalinha():
    print('\n')

def leia(prompt=""):
    return input(prompt)

def inteiro(valor):
    return int(valor)

def real(valor):
    return float(valor)

def cadeia(valor):
    return str(valor)

def boleano(valor):
    return bool(valor)

def executar(instrucao):
    return lambda: instrucao

'''versão velhas
def executar(instrucao):
    if callable(instrucao):
        return instrucao
    return lambda: instrucao

def executar(instrucao):
    return lambda: eval(instrucao, globals(), locals())
'''
def seVerdadeiro(*instrucoes):
    return tuple(lambda instr=instr: instr() for instr in instrucoes)

def seFalso(*instrucoes):
    return tuple(lambda instr=instr: instr() for instr in instrucoes)


#Versão nova

def se(condicao, entao, senao=None):
    if condicao:
        for instrucao in entao:
            instrucao()
    elif senao is not None:
        for instrucao in senao:
            instrucao()


''' #Versão antiga para registro
def se(condicao, entao, senao=None):
    if condicao:
        entao()
    elif senao is not None:
        senao()
'''


def enquanto(condicao_func, corpo_func):
    while condicao_func():
        corpo_func()

def repita(vezes, corpo_func):
    for _ in range(vezes):
        corpo_func()

def faca(corpo_func, condicao_func):
    while True:
        corpo_func()
        if not condicao_func():
            break

def escolha(valor, casos):
    if valor in casos:
        casos[valor]()
    elif 'padrao' in casos:
        casos['padrao']()

def E(a, b):
    return a and b

def OU(a, b):
    return a or b

def NAO(a):
    return not a

def pula():
    return '\n'

caractere = str
longo = int
