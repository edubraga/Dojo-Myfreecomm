# coding: UTF-8

lista_das_notas = (100, 50, 20, 10)

def caixa_eletronico(valor):
    resultado = []
    for nota in lista_das_notas:
        while valor >= nota:
            resultado.append(nota)
            valor -= nota

    return tuple(resultado)

