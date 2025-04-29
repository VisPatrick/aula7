# Funçoes em python inicia com a palavra def
# reservada def
# Função são rotinas que podem ser chamadas em qualquer parte do código
# Funções podem receber parâmetros e retornar valores
# São blocos de códigos que só serão executado, se forem chamados

def saudacao():
    print("\nOlá mundo")    # entros dos parênteses estão os argumentos


saudacao()  # chamando a função
saudacao()  # chamando a função
saudacao()  # chamando a função

def mostrar_linha():
    print(30*'=')  # imprime 30 vezes o caractere '-'


mostrar_linha
print('\nMódulo 01')
mostrar_linha
print('ALGORITIMOS')
mostrar_linha
print('ANALISE DE DADOS')
mostrar_linha

# Função com parâmetros


def saudacao(texto):  # def é a palavra reservada para definir uma função
    print(f"\nOlá {texto}!")    # entros dos parênteses estão os argumentos


nome = input('Digite seu nome: ')
saudacao(nome)  # chamando a função

def soma(a, b):
    s = a + b  # soma dos dois números
    print(s)

soma(4, 5)  # chamando a função

def somar(a, b):
    s = a + b  # soma dos dois números
    # print("\n", s)
    return s  # retorna o valor da soma


soma = somar(4, 5)  # chamando a função
print(f'\nA soma é {soma}')  # chamando a função


def somar_numeros(x, y):
    s = x + y
    return s


for i in range(3):
    n1 = int(input('\n''Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))

    soma = somar_numeros(n1, n2)
    print(f'A soma de {n1} + {n2} = {soma}')    