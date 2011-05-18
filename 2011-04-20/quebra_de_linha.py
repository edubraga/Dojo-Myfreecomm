# coding: UTF-8


def quebra_de_linha(frase):
    resposta = []
    quebra_frase(resposta, frase)
    return '\n'.join(resposta)



def quebra_frase(buf, frase):
    indice = -1

    if len(frase) > 20:
        for i in xrange(20, -1, -1):
            if frase[i] == ' ':
                indice = i
                break
        if indice == -1:
            for i in xrange(19, len(frase)):
                if frase[i] == ' ':
                    indice = i
                    break

    if indice == -1:
        buf.append(frase)
    else:
        buf.append(frase[:indice].strip())
        quebra_frase(buf, frase[indice:].strip())
