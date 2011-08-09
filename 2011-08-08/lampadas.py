# coding: UTF-8


def lampadas(num):
    if num == 0:
        return []
    else:
        resultado = lampadas(num - 1)
        div = numero_divisores(num)
        resultado.append(div % 2)
        return resultado


def numero_divisores(num):    
    cont = 1
    for i in range(1, num):
        if num % i == 0:
            cont += 1
        
    return cont
