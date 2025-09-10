'''
Cristiano Teixeira
'''
def escreva(*args, sep=' ', end='\n'):
    print(*args, sep=sep, end=end)

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
    return lambda: eval(instrucao)

def se(condicao, entao, senao=None):
    if condicao:
        if callable(entao):
            entao()
        else:
            escreva(entao)
    elif senao is not None:
        if callable(senao):
            senao()
        else:
            escreva(senao)


'''def se(condicao, entao, senao=None):
    if condicao:
        entao()
    elif senao:
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
