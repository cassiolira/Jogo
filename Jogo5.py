print('Welcome to Guess What? Game')
print('***************************')
print('***************************')

# A função random é necessário ser importada pois não é build in
import random as rd

# rd.random() gera um numero de 0 a 1, mas podemos utilizar a função rd.randgange(0,101)
numero_secreto = int(rd.random()*100)

# Vamos incluir uma seleção de dificuldades do jogo, escolhida pelo Usuário

level_str = input('Please, select your level: Type (1) for Easy, (2) for Normal or (3) for Master Level')
level = int(level_str)
if (level == 1):
    print('You selected te Easy Level')
    tentativas = 12
elif (level == 2):
    print('You selected te Normal Level')
    tentativas = 8
elif (level == 3):
    print('You selected te Master Level')
    tentativas = 5
else:
    print('Wrong number!')


# Início do código do jogo.
for rodadas in range(1, tentativas + 1):
    print('Try', rodadas, 'of', tentativas)
    chute_str = input('Enter a number between 0 to 100:')
    chute = int(chute_str)
    print('You typed: ', chute)

    if (0 > chute or chute > 100):
        print('Please, out of range, choose a number between 0 to 100!')
        continue
    else:
        if (numero_secreto == chute):
            print('Congratulation! You got it!')
            break
        else:
            if (numero_secreto < chute):
                print('You lose! Your number is bigger than the secret number!')
            else:
                print('You lose! Your number is smaller than the secret number!')

print('End of game!')