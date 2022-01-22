def jogar():

    print('****Forca Game!****')

    palavra_secreta = 'Python'

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        chute = input('Qual letra você deseja chutar?')
        index = 1
        for letra in palavra_secreta:
            if (chute==letra):
                print('Você advinhou a letra:',chute,'na posição', index)
            index = index + 1
        print('Continue jogando...')

    print('Final do Jogo!')
    #Serve para definir se o programa foi rodado pelo menu ou se foi utilizado
    #forma direta.
if(__name__ == '__main__'):
    jogar()