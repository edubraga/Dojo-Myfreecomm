# coding: UTF-8

def intervalos(lista):
    if len(lista) == 1:
        return '[{0}]'.format(lista[0])

    elif len(lista) == lista[-1] - lista[0] + 1:
        return '[{0}-{1}]'.format(lista[0], lista[-1])

    else:
        i = 1
        while i < len(lista):
            if lista[i] - lista[i-1] > 1:
                return '{0}, {1}'.format(
                    intervalos(lista[:i]), intervalos(lista[i:]))
            i += 1
