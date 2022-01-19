import forca
import adivinha_final

print('*************************')
print('****Choose your game!****')
print('*************************')

print('What game do you wanna play?')

jogo = int(input(print('Type (1) for Guess What or (2) for Forca ')))

if (jogo == 2):
    forca.jogar()
elif (jogo ==1):
    adivinha_final.jogar()