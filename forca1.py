import random

def jogar():

    print('****Forca Game!****')

    #Geração de uma lista randomica.
    
    arquivo = open('palavras.txt')
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ['_' for letra in palavra_secreta]

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
                    letras_acertadas[index] = letra
                    print('Tem a letra', chute, 'na posição', index + 1)
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