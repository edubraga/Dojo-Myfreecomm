# coding: UTF-8


from unittest import TestCase, main
from intervalos import intervalos


class TestIntervalos(TestCase):

    def test_sequencia_curta_continua(self):
        entrada = [1, 2, 3]
        saida_esperada = '[1-3]'
        saida = intervalos(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_sequencia_maiorzinha_continua(self):
        entrada = range(1, 121)
        saida_esperada = '[1-120]'
        saida = intervalos(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_sequencia_grande_continua(self):
        entrada = range(1, 10001)
        saida_esperada = '[1-10000]'
        saida = intervalos(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_sequencia_5_100(self):
        entrada = range(5, 101)
        saida_esperada = '[5-100]'
        saida = intervalos(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_sequencia_curta_descontinua(self):
        entrada = [1, 2, 4, 5]
        saida_esperada = '[1-2], [4-5]'
        saida = intervalos(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_sequencia_duplamente_descontinua(self):
        entrada = [1, 2, 4, 5, 6, 7, 10, 11, 12]
        saida_esperada = '[1-2], [4-7], [10-12]'
        saida = intervalos(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_sequencia_duplamente_descontinua(self):
        entrada = [1, 2, 4, 5, 6, 7, 10, 11, 12, 150]
        saida_esperada = '[1-2], [4-7], [10-12], [150]'
        saida = intervalos(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_um_unico_elemento(self):
        entrada = [45]
        saida_esperada = '[45]'
        saida = intervalos(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_lista_do_exemplo(self):
        entrada = [100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150]
        saida_esperada = '[100-105], [110-111], [113-115], [150]'
        saida = intervalos(entrada)
        self.assertEqual(saida, saida_esperada)


if __name__ == '__main__':
    main()
