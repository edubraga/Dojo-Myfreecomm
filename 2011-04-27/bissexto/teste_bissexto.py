# coding: UTF-8

from unittest import TestCase, main
from ano_bissexto import eh_bissexto

class TestBissexto(TestCase):

    def test_1600(self):
        entrada = 1600

        bissexto = eh_bissexto(entrada)
        self.assertTrue(bissexto)
        
    def test_1742(self):
        entrada = 1742

        bissexto = eh_bissexto(entrada)
        self.assertFalse(bissexto)

    def test_1732(self):
        entrada = 1732

        bissexto = eh_bissexto(entrada)
        self.assertTrue(bissexto)

    def test_2000(self):
        entrada = 2000

        bissexto = eh_bissexto(entrada)
        self.assertTrue(bissexto)

    def test_1900(self):
        entrada = 1900

        bissexto = eh_bissexto(entrada)
        self.assertFalse(bissexto)

if __name__ == '__main__':
    main()
