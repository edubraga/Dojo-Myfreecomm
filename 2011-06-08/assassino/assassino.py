# coding: UTF-8

from random import choice


def assassino(acho_que, real):
    if acho_que == real:
        return 0

    else:
        retornos_possiveis = []
        
        for i, valor in enumerate(acho_que):
            if valor != real[i]:
                retornos_possiveis.append(i + 1)

        return choice(retornos_possiveis)


class Detetive(object):

    suspeito_atual = 1
    local_atual = 1
    arma_atual = 1

    def proximo_chute(self, resultado=None):

        if resultado == 1:
            self.suspeito_atual += 1

        elif resultado == 2:
            self.local_atual += 1

        elif resultado == 3:
            self.arma_atual += 1

        return (
            self.suspeito_atual,
            self.local_atual,
            self.arma_atual,
        )

