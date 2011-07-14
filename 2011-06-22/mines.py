# coding: UTF-8


def campo_minado(campo):
    largura = len(campo[0])-1
    altura = len(campo)-1

    resultado = []

    for y, linha in enumerate(campo):
        linha_resultante = []
        for x, elemento in enumerate(linha):
            if elemento == '*':
                linha_resultante.append(elemento)
            else:
                x_min = x - 1
                x_min = x_min if x_min >= 0 else 0
                x_max = x + 1
                x_max = x_max if x_max <= largura else largura

                y_min = y - 1
                y_min = y_min if y_min >= 0 else 0
                y_max = y + 1
                y_max = y_max if y_max <= altura else altura
                
                linha_resultante.append(''.join(aux[x_min:x_max+1] for aux in campo[y_min:y_max+1]).count('*'))
        resultado.append(''.join(str(aux) for aux in linha_resultante))
    return tuple(resultado)

