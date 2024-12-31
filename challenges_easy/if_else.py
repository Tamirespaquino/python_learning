'''
Desafio do steak

Criar um programa que, dependendo da temperatura, em Celsius, do Steak, ele retorna o ponto de cozimento em portugues.
O usuário deverá fornecer a temperatura.

Temperaturas - Cozimento
120ºF ou 48ºC - Rare (selada)
130ºF ou 54ºC - Medium rare (ao ponto para o mal passado)
140ºF ou 60ºC - Medium (Ao ponto)
150ºF ou 65ºC - Medium well (ao ponto para o bem passado)
160ºF ou 71ºC - Well done (Bem passado)
'''

pedido_usuario = int(input('Qual a temperatura do seu Steak? '))

if pedido_usuario < 48:
    print('Cozinhar por mais alguns minutos')
if pedido_usuario in range(48, 53):
    print('Rare (selada)')
elif pedido_usuario in range(44, 59):
    print('Medium rare (ao ponto para o mal passado)')
elif pedido_usuario in range(60, 64):
    print('Medium (Ao ponto)')
elif pedido_usuario in range(65, 70):
    print('Medium well (ao ponto para o bem passado)')
elif pedido_usuario >= 71:
    print('Well done (Bem passado)')

