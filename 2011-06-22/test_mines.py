# coding: UTF-8

from unittest import TestCase, main
from mines import campo_minado


class TestMines(TestCase):

    def test_1x1_sem_minas(self):
        entrada = ('.',)
        saida_esperada = ('0',)
        saida = campo_minado(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_1x1_com_mina(self):
        entrada = ('*',)
        saida_esperada = ('*',)
        saida = campo_minado(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_2x2_sem_minas(self):
        entrada = (
            '..',
            '..',
        )
        saida_esperada = (
            '00',
            '00',
        )
        saida = campo_minado(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_2x2_com_1_mina(self):
        entrada = (
            '.*',
            '..',
        )
        saida_esperada = (
            '1*',
            '11',
        )
        saida = campo_minado(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_2x2_com_2_minas_em_linha(self):
        entrada = (
            '**',
            '..',
        )
        saida_esperada = (
            '**',
            '22',
        )
        saida = campo_minado(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_2x2_com_2_minas_em_coluna(self):
        entrada = (
            '*.',
            '*.',
        )
        saida_esperada = (
            '*2',
            '*2',
        )
        saida = campo_minado(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_2x2_com_2_minas_em_diagonal(self):
        entrada = (
            '*.',
            '.*',
        )
        saida_esperada = (
            '*2',
            '2*',
        )
        saida = campo_minado(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_3x5_com_minas_aleatorias(self):
        entrada = (
            '...',
            '..*',
            '...',
            '*..',
            '.*.',
        )
        saida_esperada = (
            '011',
            '01*',
            '121',
            '*21',
            '2*1',
        )
        saida = campo_minado(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_5X7_com_minas_aleatorias(self):
        entrada = (
            '..***',
            '.....',
            '..**.',
            '*....',
            '....*',
            '.*...',
            '....*',

        )
        saida_esperada = (
            '01***',
            '02453',
            '12**1',
            '*2232',
            '2211*',
            '1*122',
            '1111*',
        )
        saida = campo_minado(entrada)
        self.assertEqual(saida, saida_esperada)

if __name__ == "__main__":
    main()

