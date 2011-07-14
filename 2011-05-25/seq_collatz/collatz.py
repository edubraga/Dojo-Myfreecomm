# -*- coding: utf-8 -*-

def sequencia_collatz(numero):
    sequencia = [numero]
    while numero != 1:
        numero = proximo_numero(numero)
        sequencia.append(numero)
    return sequencia

def e_par(numero):
    return numero % 2 == 0

def proximo_numero(numero):
    if e_par(numero):
        return numero / 2
    else:
        return 3 * numero + 1
