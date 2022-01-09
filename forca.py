from random import randint

# Variáveis
palavra = 'camisa'

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


while True:

    linha('Digite uma letra')
    letra = input("Digite a letra desejada: ").strip().lower()[0]

    if letra in palavra:
        linha(f"Encontrada a letra {letra}")
    else:
        linha(f"Não encontrada a letra {letra}")
