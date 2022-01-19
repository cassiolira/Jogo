print('Welcome to Guess What? Game')
print('***************************')
print('***************************')

# A função random é necessário ser importada pois não é build in
import random as rd

# rd.random() gera um numero de 0 a 1, mas podemos utilizar a função rd.randgange(0,101)
numero_secreto = int(rd.random()*100)

tentativas_str = input('How many attempts do you want?')
print('You chose:', tentativas_str)
print('You will have', tentativas_str, 'chances!')
# È necessário converter o tentativas_str, que é uma variável string, numa variável integer, neste caso tentativas_int,
# usando a função INT
tentativas_int = int(tentativas_str)

# Início do código do jogo.
for rodadas in range(1, tentativas_int):
    print('Try', rodadas, 'of', tentativas_int)
    chute_str = input('Enter a number between 0 to 100:')
    print('You typed:: ', chute_str)
    # È necessário converter o chute_str, que é uma variável string, numa variável integer, neste caso chute_int,
    # usando a função INT
    chute_int = int(chute_str)
    if (0 > chute_int or chute_int > 100):
        print('Please, out of range, choose a number between 0 to 100!')
        continue
    else:
        if (numero_secreto == chute_int):
            print('Congratulation! You got it!')
            break
        else:
            if (numero_secreto < chute_int):
                print('You lose! Your number is bigger than the secret number!')
            else:
                print('You lose! Your number is smaller than the secret number!')

print('End of game!')
