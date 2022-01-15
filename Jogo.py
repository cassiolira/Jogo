print('Welcome to Guess What? Game')
print('***************************')
print('***************************')

numero_secreto = 42

tentativas_str = input('How many attempts do you want?')
print('You chose:', tentativas_str)
print('You will have', tentativas_str, 'chances!')
# È necessário converter o tentativas_str, que é uma variável string, numa variável integer, neste caso tentaivas_int,
# usando a função INT
tentativas_int = int(tentativas_str)

# Início do código do jogo.
while (tentativas_int > 0):

    chute_str = input('Enter your number:')
    print('You typed:: ', chute_str)
    # È necessário converter o chute_str, que é uma variável string, numa variável integer, neste caso chute_int,
    # usando a função INT
    chute_int = int(chute_str)

    if (numero_secreto == chute_int):
            print('Congratulation! You got it!')
            tentativas_int = 0
    else:
        if (numero_secreto < chute_int):
            print('You lose! Your number is bigger than the secret number!')
        if (numero_secreto > chute_int):
            print('You lose! Your number is smaller than the secret number!')

    tentativas_int = tentativas_int - 1

print('End of game!')
