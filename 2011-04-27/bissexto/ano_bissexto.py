# coding: UTF-8

def eh_bissexto(ano):
    return (ano % 400 == 0) or (ano % 4 == 0) and (ano % 100 > 0)
