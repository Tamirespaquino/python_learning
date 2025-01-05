# Desafio funções

'''
Criar um programa de calcula a quantidade de tinta necessária para
pintar uma parede. O usuário deverá fornecer as seguintes
informações: Rendimento, altura e largura.
O programa deve mostrar na tela a mensagem 'Você necessita de x latas de tinta'.
'''

rendimento = int(input('Qual é o rendimento da lata de tinta? '))
altura = int(input('Qual é a altura da parede? '))
largura = int(input('Qual é a larugra da parede? '))

def quantidade_lata():
    quantidade_total = (altura * largura)/rendimento
    print(f'Você necessita de {quantidade_total} de latas de tinta.')

quantidade_lata()