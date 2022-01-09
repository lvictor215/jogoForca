from random import randint

# Variáveis
palavras = ['camisa', 'short', 'tenis',
            'sapato', 'calça', 'bone', 'meia', 'bermuda']
palavra = ''
digitadas = list()
tentativas = 6
contador = 0
var = ''
pronta = list()


def linha(msg='', tamanho=50, caractere='='):
    print(caractere * tamanho)
    print(msg.center(tamanho))
    print(caractere * tamanho)


def validar():
    global tentativas
    if tentativas == 6:
        print('=' * 50)
        print('o'.center(50))
        print('-|-'.center(50))
        print('_ _'.center(50))
    elif tentativas == 5:
        print('=' * 50)
        print('o'.center(50))
        print('-|-'.center(50))
        print('_  '.center(50))
    elif tentativas == 4:
        print('=' * 50)
        print('o'.center(50))
        print('-|-'.center(50))
        print('   '.center(50))
    elif tentativas == 3:
        print('=' * 50)
        print('o'.center(50))
        print('-| '.center(50))
        print(''.center(50))
    elif tentativas == 2:
        print('=' * 50)
        print('o'.center(50))
        print('|'.center(50))
        print(''.center(50))
    elif tentativas == 1:
        print('=' * 50)
        print('o'.center(50))
        print(''.center(50))
        print(''.center(50))


palavra = palavras[randint(0, len(palavras) - 1)]

while tentativas > 0:

    for x in range(0, len(palavra)):
        flag = 0
        for y in range(0, len(pronta)):
            if x == pronta[y]:
                var += pronta[y - 1]
                flag = 1
                var += ' '

        if flag == 0:
            var += '_ '
    linha(var)
    var = ''

    validar()

    while True:
        linha('Digite uma letra')
        letra = input("Digite a letra desejada: ").strip().lower()[0]
        if letra not in digitadas:
            break
        else:
            linha("Digite uma letra que não tenha sido digitada!")
    if letra in palavra:

        for a, b, in enumerate(palavra):
            if b == letra:
                contador += 1
                pronta.append(b)
                pronta.append(a)

        linha(f"Encontrada a letra {letra}")

    else:
        linha(f"Não encontrada a letra {letra}")
        tentativas -= 1

    digitadas.append(letra)

    if tentativas == 0:
        print("Você perdeu!")
        print("A palavra correta era:")
        linha(palavra)
    elif len(pronta) == len(palavra) * 2:
        print("Você ganhou!")
        print(f"A palavra era {palavra}")
        break
