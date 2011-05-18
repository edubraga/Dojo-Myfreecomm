# -*- coding utf-8 -*- 

from math import ceil, sqrt


def palavra_eh_prima(entrada):
    soma = soma_das_letras(entrada)
    return eh_primo(soma)


def eh_primo(numero):
    if numero == 1:
        return False
    elif numero == 2:
        return True
    else:
        return all(
            (numero % i) for i in xrange(2, int(ceil(sqrt(numero)))+1)
        )


def soma_das_letras(palavra):
    soma = 0
    for cada_letra in palavra:
        soma += valor_da_letra(cada_letra)
    return soma


def valor_da_letra(letra):
    if "a" <= letra <= "z":
        return ord(letra) - ord("a") + 1
    elif "A" <= letra <= "Z":
        return ord(letra) - ord("A") + 27
    else:
        return 0
