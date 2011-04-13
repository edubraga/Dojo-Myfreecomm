# coding: UTF-8


def capitalize(x):
    if x in ('de', 'da', 'das', 'do', 'dos'):
        return x
    else:
        return x.capitalize()


def separa_nome_sobrenome(nome):
    aux = nome.lower().split()
    if len(aux) > 2 and aux[-1] in ('junior', 'filho', 'neto'):
        return ' '.join(aux[-2:]), aux[:-2]
    else:
        return aux[-1], aux[:-1]



def nomes_de_autor(nome):
    sobrenome, pre_nome = separa_nome_sobrenome(nome)
    resp = [sobrenome.upper() + ',']
    resp.extend(capitalize(x) for x in pre_nome)

    return ' '.join(resp)

