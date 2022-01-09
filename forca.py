from random import randint

# Variáveis
palavra = 'camisa'
digitadas = list()
tentativas = 3
contador = 0
var = ''
pronta = list()

# funções

# def inputint(msg=''):
#     while True:
#         vlr = input(msg).strip()
#         try:
#             vlr = int(vlr)
#             break
#         except:
#             print("Erro! Apenas números inteiros são permitidos, tente novamente!")
#     return vlr


def linha(msg='', tamanho=50, caractere='='):
    print(caractere * tamanho)
    print(msg.center(tamanho))
    print(caractere * tamanho)


while tentativas > 0:

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

    digitadas.append(letra)

    for x in range(0, len(palavra)):
        flag = 0
        for y in range(0, len(pronta)):
            if x == pronta[y]:
                var += pronta[y - 1]
                flag = 1

        if flag == 0:
            var += '_'
    linha(var)
    var = ''

    if len(pronta) == len(palavra) * 2:
        print("Você ganhou!")
        break
    elif tentativas == 0:
        print("Você perdeu!")

print(digitadas)
print(pronta)
