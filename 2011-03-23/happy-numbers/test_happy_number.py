import unittest
from happy_number import numero_feliz

class TestHappyNumbers(unittest.TestCase):

    def test_numero_1_feliz(self):
        self.assertTrue(numero_feliz(1))

    def test_numero_2_nao_feliz(self):
        self.assertFalse(numero_feliz(2))

    def test_numero_3_nao_feliz(self):
        self.assertFalse(numero_feliz(3))

    def test_numero_4_nao_feliz(self):
        self.assertFalse(numero_feliz(4))

    def test_numero_5_nao_feliz(self):
        self.assertFalse(numero_feliz(5))

    def test_numero_7_feliz(self):
        self.assertTrue(numero_feliz(7))

    def test_numero_10_feliz(self):
        self.assertTrue(numero_feliz(10))

    def test_numero_13_feliz(self):
        self.assertTrue(numero_feliz(13))

    def test_numero_19_feliz(self):
        self.assertTrue(numero_feliz(19))

    def test_numero_crazy_feliz(self):
        self.assertFalse(numero_feliz(1034567892987654301))

unittest.main()
