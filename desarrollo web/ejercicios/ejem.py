import random


regalos = ['sartén', 'jamón', 'mp4', 'muñeca', 'tv',
           'patín', 'balón', 'reloj', 'bicicleta', 'anillo']

for serie in range(2):
    print('\nserie:', serie + 1)
    random.seed(0)
    for sorteo in range(5):
        regalo = regalos[random.randint(0, 9)]
        print('Sorteo', sorteo + 1, ':', regalo)