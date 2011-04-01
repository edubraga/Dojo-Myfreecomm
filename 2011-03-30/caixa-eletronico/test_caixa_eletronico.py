#!/usr/bin/env python
# coding: UTF-8

from unittest import TestCase, main

from caixa_eletronico import caixa_eletronico


class TestCaixaEletronico(TestCase):

    def test_10(self):
        parametro = 10
        esperado = (10,)
        retornado = caixa_eletronico(parametro)
        self.assertEqual(retornado, esperado)

    def test_20(self):
        parametro = 20
        esperado = (20,)
        retornado = caixa_eletronico(parametro)
        self.assertEqual(retornado, esperado)

    def test_30(self):
        parametro = 30
        esperado = (20, 10)
        retornado = caixa_eletronico(parametro)
        self.assertEqual(retornado, esperado)

    def test_40(self):
        parametro = 40
        esperado = (20, 20)
        retornado = caixa_eletronico(parametro)
        self.assertEqual(retornado, esperado)

    def test_50(self):
        parametro = 50
        esperado = (50,)
        retornado = caixa_eletronico(parametro)
        self.assertEqual(retornado, esperado)

    def test_60(self):
        parametro = 60
        esperado = (50, 10)
        retornado = caixa_eletronico(parametro)
        self.assertEqual(retornado, esperado)

    def test_70(self):
        parametro = 70
        esperado = (50, 20)
        retornado = caixa_eletronico(parametro)
        self.assertEqual(retornado, esperado)

    def test_100(self):
        parametro = 100
        esperado = (100,)
        retornado = caixa_eletronico(parametro)
        self.assertEqual(retornado, esperado)

    def test_1990(self):
        parametro = 1990
        esperado = (100,) * 19 + (50, 20, 20)
        retornado = caixa_eletronico(parametro)
        self.assertEqual(retornado, esperado)

if __name__ == '__main__':
    main()
