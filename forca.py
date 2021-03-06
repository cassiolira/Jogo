def jogar():

    print('****Forca Game!****')
    #palavra_secreta não é uma list e sim um tuple, é imutável, por isso usamos parenteses
    #ao inves de colchete
    palavra_secreta = ('PYTHON')
    letras_acertadas = ['_','_','_','_','_','_']

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        chute = input('Qual letra você deseja chutar?')
        #Vamos retirar o espaço com a função strip()
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    print('Você advinhou a letra:',chute,'na posição', index + 1)
                    letras_acertadas[index] = letra
                    print(letras_acertadas)
                    print('Continue jogando...')
                index = index + 1
        else:
            erros = erros + 1

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print('Você ganhou!!!')
    else:
        print('Você foi enforcado!!!')
    print('Final do Jogo!')
    #Serve para definir se o programa foi rodado pelo menu ou se foi utilizado
    #forma direta.
if(__name__ == '__main__'):
    jogar()