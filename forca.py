from random import randint
# Variáveis
palavras = ['cabelo', 'pescoço', 'orelha', 'boca', 'nariz']
palavra_sorteada = ''
tamanho_sorteada = 0
tamanho_digitada = 0
palavra_validacao = ''
letras_digitadas = ''
chance = 0

# funções


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


def newGame():
    global palavra_sorteada
    global palavra_validacao
    global letras_digitadas
    global tamanho_sorteada
    global chance

    chance = 6
    palavra_sorteada = palavras[randint(0, len(palavras)-1)]
    for a in range(0, len(palavra_sorteada) - 1):
        palavra_validacao += ' '

    letras_digitadas = ''
    tamanho_sorteada = len(palavra_sorteada)


def validar(letra):
    global palavra_validacao
    contador = 0

    for a, b in enumerate(palavra_sorteada):
        if letra == b:
            palavra_validacao[a] = letra
            contador += 1
    return int(contador)


while True:
    linha("Bem vindo ao jogo da velha!")
    print("Escolha uma opção na lista abaixo:")
    print('[1] Iniciar um novo jogo')
    print('[2] Sair do jogo')

    opcao = inputint('Escolha a opção desejada: ')

    if opcao == 1:
        newGame()
        linha(f"A palavra escolhida tem {len(palavra_sorteada)} letras!")
        print(f'{"_ " * len(palavra_sorteada)}'.center(50))
        print()
        while True:
            escolhido = input("Digite a letra desejada: ").lower().split()[0]
            if escolhido in palavra_sorteada and escolhido not in letras_digitadas:
                print('Tem essa letra lá')
                tamanho_digitada += validar(escolhido)
                letras_digitadas += escolhido
            else:
                print('Não tem essa letra lá')
                letras_digitadas += escolhido

            if tamanho_digitada == tamanho_sorteada:
                linha("Parabéns! Você Venceu!")
                break
            elif chance == 0:
                linha("Que pena... Você perdeu!")
                break

    elif opcao == 2:
        break

    else:
        print("ERRO! Escolha apenas uma dentre as opções escolhidas!")
