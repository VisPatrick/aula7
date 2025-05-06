# quantidade máxima de peixes 100
# se utrapassar  100 peixes , o pescador paga uma multa de 4 reais por quilo excedente
# programa simples  para verificar se haverá multa ou não, se ultrapassar o limite de  peixe 

limite = 100

# ENTRADA


def calcular_multa(n):
    multa = limite * 4
    return multa


peso = float(input('\nDigite o peso do peixe: '))


if peso > limite:
    multa = calcular_multa(peso)
    print(f'\nVocê ultrapassou o limite de {limite} quilos de peixe')
    print(f'\nVocê deve pagar {multa} reais de multa')
else:
    print(f'\nVocê não ultrapassou o limite de {limite} quilos de peixe')