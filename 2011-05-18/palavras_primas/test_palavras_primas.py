# -*- coding utf-8 -*- 

from unittest import TestCase, main

from palavras_primas import palavra_eh_prima

class TestPalavrasPrimas(TestCase):

    def test_a_retorna_False(self):
        entrada = "a"

        retorno = palavra_eh_prima(entrada)

        self.assertFalse(retorno)

    def test_b_retorna_True(self):
        entrada = "b"

        retorno = palavra_eh_prima(entrada)

        self.assertTrue(retorno)

    def test_d_retorna_False(self):
        entrada = "d"

        retorno = palavra_eh_prima(entrada)

        self.assertFalse(retorno)

    def test_ab_retorna_True(self):
        entrada = "ab"

        retorno = palavra_eh_prima(entrada)

        self.assertTrue(retorno)

    def test_ac_retorna_False(self):
        entrada = "ac"

        retorno = palavra_eh_prima(entrada)

        self.assertFalse(retorno)

    def test_aab_retorna_False(self):
        entrada = "aab"

        retorno = palavra_eh_prima(entrada)

        self.assertFalse(retorno)

    def test_aab_retorna_False(self):
        entrada = "Aa"

        retorno = palavra_eh_prima(entrada)

        self.assertFalse(retorno)

    def test_aab_retorna_False(self):
        entrada = "a a a a"

        retorno = palavra_eh_prima(entrada)

        self.assertFalse(retorno)

if __name__ == '__main__':
    main()
