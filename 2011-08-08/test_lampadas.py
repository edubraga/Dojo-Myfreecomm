# coding: UTF-8

from unittest import TestCase, main
from lampadas import lampadas


class TestLampadas(TestCase):

    def test_1(self):
        entrada = 1
        esperado = [1]
        saida = lampadas(entrada)
        self.assertEqual(esperado, saida)

    def test_2(self):
        entrada = 2
        esperado = [1, 0]
        saida = lampadas(entrada)
        self.assertEqual(esperado, saida)

    def test_3(self):
        entrada = 3
        esperado = [1, 0, 0]
        saida = lampadas(entrada)
        self.assertEqual(esperado, saida)

    def test_4(self):
        entrada = 4
        esperado = [1, 0, 0, 1]
        saida = lampadas(entrada)
        self.assertEqual(esperado, saida)

    def test_5(self):
        entrada = 5
        esperado = [1, 0, 0, 1, 0]
        saida = lampadas(entrada)
        self.assertEqual(esperado, saida)

    def test_6(self):
        entrada = 6
        esperado = [1, 0, 0, 1, 0, 0]
        saida = lampadas(entrada)
        self.assertEqual(esperado, saida)

    def test_7(self):
        entrada = 7
        esperado = [1, 0, 0, 1, 0, 0, 0]
        saida = lampadas(entrada)
        self.assertEqual(esperado, saida)

    def test_8(self):
        entrada = 8
        esperado = [1, 0, 0, 1, 0, 0, 0, 0]
        saida = lampadas(entrada)
        self.assertEqual(esperado, saida)

    def test_9(self):
        entrada = 9
        esperado = [1, 0, 0, 1, 0, 0, 0, 0, 1]
        saida = lampadas(entrada)
        self.assertEqual(esperado, saida)

    def test_10(self):
        entrada = 10
        esperado = [1, 0, 0, 1, 0, 0, 0, 0, 1, 0]
        saida = lampadas(entrada)
        self.assertEqual(esperado, saida)

    def test_11(self):
        entrada = 11
        esperado = [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
        saida = lampadas(entrada)
        self.assertEqual(esperado, saida)

    def test_12(self):
        entrada = 12
        esperado = [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]
        saida = lampadas(entrada)
        self.assertEqual(esperado, saida)




if __name__ == '__main__':
    main()

