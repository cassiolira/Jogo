def jogar():
    print('****Punch Game!****')


    vida = input('Type the life of the Monster:')
    vida_int = int(vida)
    forca = input('Type your Punch Power:')
    forca_int = int(forca)
    turno = (vida_int/forca_int)
    print('The monster will die with ', turno, 'punch!')

#Serve para definir se o programa foi rodado pelo menu ou se foi utilizado
#forma direta.
if(__name__ == __main__):
    jogar()