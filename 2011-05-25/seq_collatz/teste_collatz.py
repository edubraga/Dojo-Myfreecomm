# -*- coding: utf-8 -*-

from unittest import TestCase, main

from collatz import sequencia_collatz

class TesteCollatz(TestCase):

    def teste_entrada_2(self):
        self.assertEquals(sequencia_collatz(2), [2,1])

    def teste_entrada_4(self):
        self.assertEquals(sequencia_collatz(4), [4,2,1])

    def teste_entrada_8(self):
        self.assertEquals(sequencia_collatz(8), [8,4,2,1])

    def teste_entrada_3(self):
        self.assertEquals(sequencia_collatz(3), [3, 10, 5, 16, 8, 4, 2, 1])

    def teste_entrada_13(self):
        self.assertEquals(sequencia_collatz(13), [13, 40, 20, 10, 5, 16, 8, 4, 2, 1])

if __name__ == '__main__':
    main()
