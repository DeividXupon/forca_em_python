import random

def jogar():

    msg_introdutoria()

    palavra = palavra_aleatoria()
    lista_de_letras = ["?" for letra in palavra]

    erros = 0
    acerto = False
    perdeu = False

    while not acerto and not perdeu:
        palavra_mostrada = ""

        espaco_vazi()
        chute = input("|    Digite uma letra:  ")
        chute = chute.strip().upper()
        espaco_vazi()

        if len(chute) >= 2:
            print("|*-*- *- *-* APENAS UM DIGITO! *-*  -* -*-*|")
            continue

        posicao = 0

        if chute in palavra.upper():
            str_posicao = "0"
            for letra in palavra:
                if chute == letra.upper():
                    print("|+", "-" * 40, "+|", sep="")
                    print(f"||Achou a letra {chute} na posição {posicao}"," "*(13 - len(str_posicao)),"||",sep="")
                    lista_de_letras[posicao] = chute
                posicao = posicao + 1
                str_posicao = str(posicao)
        else:
            print("|+","-"*40,"+|", sep="")
            print(f"|| A letra -> {chute} <- Não foi encontrada :(  ||")
            print("|+", "-" *40, "+|", sep="")
            espaco_vazi()
            erros += 1

        for item in lista_de_letras:
            palavra_mostrada += item

        acerto = "?" not in palavra_mostrada
        perdeu = erros == 7

        desenha_forca(erros, palavra_mostrada)

    mensagem_final(acerto, palavra)

#def´s
def espaco_vazi():
    print("|", " " * 40, "|")

def msg_introdutoria():
    print(".", "_" * 42, ".", sep="")
    print("|", " " * 14, " Jogo de Forca ", " " * 13, "|", sep="")
    print("|", "~" * 42, "|", sep="")

def palavra_aleatoria():
    lista_de_palavras = []

    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            lista_de_palavras.append(linha.strip())

    numero_aleatorio = random.randrange(0, len(lista_de_palavras))
    return lista_de_palavras[numero_aleatorio]

def desenha_forca(erros, palavra):

    espaco_vazi()
    print("|█-", "█" * 38, "-█|", sep="")
    print("|  ", "█" * 8,"|/-----\_    ", " "*9, "█"*8 , "  |", sep="")

    if(erros == 1):
        print("|  ", "█" * 8, "|      (_)   ", " "*9, "█"*8 , "  |", sep="")
        print("|  ", "█" * 8, "|            ", " "*9, "█"*8 , "  |", sep="")
        print("|█-", "█" * 8, "|            ", " "*9, "█"*8 , "-█|", sep="")
        print("|  ", "█" * 8, "|            ", " "*9, "█"*8 , "  |", sep="")

    if(erros == 2):
        print("|  ", "█" * 8, "|      (_)   ", " "*9, "█"*8 , "  |", sep="")
        print("|  ", "█" * 8, "|      \     ", " "*9, "█"*8 , "  |", sep="")
        print("|█-", "█" * 8, "|            ", " "*9, "█"*8 , "-█|", sep="")
        print("|  ", "█" * 8, "|            ", " "*9, "█"*8 , "  |", sep="")

    if(erros == 3):
        print("|  ", "█" * 8, "|      (_)   ", " "*9, "█"*8 , "  |", sep="")
        print("|  ", "█" * 8, "|      \|    ", " "*9, "█"*8 , "  |", sep="")
        print("|█-", "█" * 8, "|            ", " "*9, "█"*8 , "-█|", sep="")
        print("|  ", "█" * 8, "|            ", " "*9, "█"*8 , "  |", sep="")

    if(erros == 4):
        print("|  ", "█" * 8, "|      (_)   ", " "*9, "█"*8 , "  |", sep="")
        print("|  ", "█" * 8, "|      \|/   ", " "*9, "█"*8 , "  |", sep="")
        print("|█-", "█" * 8, "|            ", " "*9, "█"*8 , "-█|", sep="")
        print("|  ", "█" * 8, "|            ", " "*9, "█"*8 , "  |", sep="")

    if(erros == 5):
        print("|  ", "█" * 8, "|      (_)   ", " "*9, "█"*8 , "  |", sep="")
        print("|  ", "█" * 8, "|      \|/   ", " "*9, "█"*8 , "  |", sep="")
        print("|█-", "█" * 8, "|       |    ", " "*9, "█"*8 , "-█|", sep="")
        print("|  ", "█" * 8, "|            ", " "*9, "█"*8 , "  |", sep="")

    if(erros == 6):
        print("|  ", "█" * 8, "|      (_)   ", " "*9, "█"*8 , "  |", sep="")
        print("|  ", "█" * 8, "|      \|/   ", " "*9, "█"*8 , "  |", sep="")
        print("|█-", "█" * 8, "|       |    ", " "*9, "█"*8 , "-█|", sep="")
        print("|  ", "█" * 8, "|      /     ", " "*9, "█"*8 , "  |", sep="")

    if (erros == 7):
        print("|  ", "█" * 8, "|      (_)   ", " "*9, "█"*8 , "  |", sep="")
        print("|  ", "█" * 8, "|      \|/   ", " "*9, "█"*8 , "  |", sep="")
        print("|█-", "█" * 8, "|       |    ", " "*9, "█"*8 , "-█|", sep="")
        print("|  ", "█" * 8, "|      / \   ", " "*9, "█"*8 , "  |", sep="")

    print("|  ", "█" * 8,"|___    -> ", palavra," "*(11 - len(palavra)),"█"*8, "  |", sep="")
    print("|  ", "█" * 8, " "*22,"█"*8,"  |", sep="")
    print("|█-","█" * 38,"-█|", sep="")
    espaco_vazi()

def mensagem_final(acerto, palavra):
    if acerto == False:
        print("|__________________________________________|")
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
    else:
        print("|__________________________________________|")
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

if __name__ == "__main__":
    jogar()
