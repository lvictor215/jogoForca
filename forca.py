from random import randint

# Variáveis
palavras = ['cabelo', 'pescoço', 'orelha', 'boca', 'nariz']
palavra_sorteada = ''
chance = 0



# funções
def newGame():
    pass

def inputint(msg=''):
    while True:
        vlr = input(msg).strip()
        try:
            vlr = int(vlr)
            break
        except:
            print("Erro! Apenas números inteiros são permitidos, tente novamente!")
    return vlr


def linha(msg='', tamanho=50, caractere='='):
    print(caractere * tamanho)
    print(msg.center(tamanho))
    print(caractere * tamanho)
