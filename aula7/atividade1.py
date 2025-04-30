# dado um número calcule o dobro, triplo e quadrado desse número para agilizar seus orçamentos
# o dobro da quantidadade solicitada (para ofertas promocionais)
# o triplo (para grandes eventos), e a área total de um adesivo , considerando que o número irformado é o lado do adesivo em cimetimetros




def calcule(n):
    n1 = n * 2
    n2 = n * 3
    n3 = n ** 2
    return n1, n2, n3


n = float(input('\n' 'Digite um número: '))

# saída


print(f'\nO dobro é {n* 2}')
print(f'\nO triplo é {n * 3}')
print(f'\nO quadrado é {n ** 2}')