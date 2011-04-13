# coding: UTF-8

from unittest import TestCase, main
from nomes import nomes_de_autor


class TestNomes(TestCase):

    def test_guimaraes_rosa(self):
        nome = nomes_de_autor("Guimaraes Rosa")
        self.assertEquals("ROSA, Guimaraes", nome)

    def test_guimaraes_rosa_minusculo(self):
        nome = nomes_de_autor("guimaraes rosa")
        self.assertEquals("ROSA, Guimaraes", nome)

    def test_edu_braga_bass(self):
        nome = nomes_de_autor("Edu Braga Bass")
        self.assertEquals("BASS, Edu Braga", nome)

    def test_noel_rosa(self):
        nome = nomes_de_autor("Noel Rosa")
        self.assertEquals("ROSA, Noel", nome)

    def test_machado_de_assis(self):
        nome = nomes_de_autor("Machado de Assis")
        self.assertEquals("ASSIS, Machado de", nome)

    def test_maria_da_penha(self):
        nome = nomes_de_autor("Maria da Penha")
        self.assertEquals("PENHA, Maria da", nome)

    def test_daiane_dos_santos(self):
        nome = nomes_de_autor("Daiane dos Santos")
        self.assertEquals("SANTOS, Daiane dos", nome)

    def test_capitao_do_nascimento(self):
        nome = nomes_de_autor("Capitao do Nascimento")
        self.assertEquals("NASCIMENTO, Capitao do", nome)

    def test_maria_das_dores(self):
        nome = nomes_de_autor("Maria das Dores")
        self.assertEquals("DORES, Maria das", nome)

    def test_edu_braga_bass_junior(self):
        nome = nomes_de_autor("Edu Braga Bass Junior")
        self.assertEquals("BASS JUNIOR, Edu Braga", nome)

    def test_jota_junior(self):
        nome = nomes_de_autor("Jota Junior")
        self.assertEquals("JUNIOR, Jota", nome)

    def test_cesar_augusto_filho(self):
        nome = nomes_de_autor("Cesar Augusto Filho")
        self.assertEquals("AUGUSTO FILHO, Cesar", nome)

    def test_joaquim_da_silva_neto(self):
        nome = nomes_de_autor("Joaquim da Silva Neto")
        self.assertEquals("SILVA NETO, Joaquim da", nome)


if __name__ == '__main__':
    main()

