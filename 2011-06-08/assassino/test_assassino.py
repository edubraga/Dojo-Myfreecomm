# coding: UTF-8

from unittest import TestCase, main
from assassino import assassino, Detetive


class TestAssassino(TestCase):

    def test_acertou_tudo_de_cara(self):
        retorno = assassino(acho_que=(1, 1, 1), real=(1, 1, 1))
        esperado = 0
        self.assertEqual(retorno, esperado)

    def test_erra_suspeito(self):
        retorno = assassino(acho_que=(2, 1, 1), real=(1, 1, 1))
        esperado = 1
        self.assertEqual(retorno, esperado)

    def test_erra_local(self):
        retorno = assassino(acho_que=(1, 2, 1), real=(1, 1, 1))
        esperado = 2
        self.assertEqual(retorno, esperado)

    def test_erra_arma(self):
        retorno = assassino(acho_que=(1, 1, 1), real=(1, 1, 2))
        esperado = 3
        self.assertEqual(retorno, esperado)

    def test_erra_suspeito_e_local(self):
        retorno = assassino(acho_que=(1, 1, 1), real=(2, 2, 1))
        esperado = (1,2)
        self.assertTrue(retorno in esperado)

    def test_erra_suspeito_e_arma(self):
        retorno = assassino(acho_que=(1, 1, 1), real=(2, 1, 2))
        esperado = (1,3)
        self.assertTrue(retorno in esperado)

    def test_erra_local_e_arma(self):
        retorno = assassino(acho_que=(1, 1, 1), real=(1, 2, 2))
        esperado = (2,3)
        self.assertTrue(retorno in esperado)

    def test_errou_tudo_de_cara(self):
        retorno = assassino(acho_que=(1, 1, 1), real=(2, 2, 2))
        esperado = (1,2,3)
        self.assertTrue(retorno, esperado)

    def test_erra_suspeito_e_local_aleatorio(self):
        retorno = [assassino(acho_que=(1, 1, 1), real=(2, 2, 1)) for _ in xrange(10)]
        self.assertFalse(reduce (lambda a, b: a == b and a, retorno))

    def test_erra_suspeito_e_arma_aleatorio(self):
        retorno = [assassino(acho_que=(1, 1, 1), real=(2, 1, 2)) for _ in xrange(10)]
        self.assertFalse(reduce (lambda a, b: a == b and a, retorno))

    def test_erra_local_e_arma_aleatorio(self):
        retorno = [assassino(acho_que=(1, 1, 1), real=(1, 2, 2)) for _ in xrange(10)]
        self.assertFalse(reduce (lambda a, b: a == b and a, retorno))

    def test_errou_tudo_de_cara_aleatorio(self):
        retorno = [assassino(acho_que=(1, 1, 1), real=(2, 2, 2)) for _ in xrange(10)]
        self.assertFalse(reduce (lambda a, b: a == b and a, retorno))


class TestDetetive(TestCase):

    def setUp(self):
        self.detetive = Detetive()

    def test_primeiro_chute(self):
        retorno = self.detetive.proximo_chute()
        esperado = (1,1,1)
        self.assertEqual(retorno, esperado)

    def test_acertou_de_cara(self):
        retorno = self.detetive.proximo_chute(0)
        esperado = (1,1,1)
        self.assertEqual(retorno, esperado)

    def test_acertou_depois_de_errar_suspeito(self):
        self.detetive.proximo_chute(1)
        retorno = self.detetive.proximo_chute(0)
        esperado = (2,1,1)
        self.assertEqual(retorno, esperado)

    def test_acertou_depois_de_errar_local(self):
        self.detetive.proximo_chute(2)
        retorno = self.detetive.proximo_chute(0)
        esperado = (1,2,1)
        self.assertEqual(retorno, esperado)

    def test_acertou_depois_de_errar_arma(self):
        self.detetive.proximo_chute(3)
        retorno = self.detetive.proximo_chute(0)
        esperado = (1,1,2)
        self.assertEqual(retorno, esperado)

    def test_segundo_chute_errando_suspeito(self):
        retorno = self.detetive.proximo_chute(1)
        esperado = (2,1,1)
        self.assertEqual(retorno, esperado)

    def test_terceiro_chute_errando_suspeito(self):
        self.detetive.proximo_chute(1)
        retorno = self.detetive.proximo_chute(1)
        esperado = (3,1,1)
        self.assertEqual(retorno, esperado)

    def test_segundo_chute_errando_local(self):
        retorno = self.detetive.proximo_chute(2)
        esperado = (1,2,1)
        self.assertEqual(retorno, esperado)

    def test_segundo_chute_errando_arma(self):
        retorno = self.detetive.proximo_chute(3)
        esperado = (1,1,2)
        self.assertEqual(retorno, esperado)

    def test_errando_suspeito_e_depois_local(self):
        self.detetive.proximo_chute(1)
        retorno = self.detetive.proximo_chute(2)
        esperado = (2,2,1)
        self.assertEqual(retorno, esperado)

    def test_errando_suspeito_e_depois_arma(self):
        self.detetive.proximo_chute(1)
        retorno = self.detetive.proximo_chute(3)
        esperado = (2,1,2)
        self.assertEqual(retorno, esperado)

    def test_errando_local_e_depois_arma(self):
        self.detetive.proximo_chute(2)
        retorno = self.detetive.proximo_chute(3)
        esperado = (1,2,2)
        self.assertEqual(retorno, esperado)


class TestCombina(TestCase):

    def test_acerta_todas(self):

        for suspeito in xrange(1,7):
            for local in xrange(1,11):
                for arma in xrange(1,7):
                    real = (suspeito,local,arma)

                    detetive = Detetive()
                    retorno = detetive.proximo_chute()
                    resultado = assassino(retorno, real)
                    while resultado != 0:
                        retorno = detetive.proximo_chute(resultado)
                        resultado = assassino(retorno, real)
                    self.assertEqual(retorno, real)

    
if __name__ == '__main__':
    main()

