# coding: UTF-8

from unittest import TestCase, main
from quebra_de_linha import quebra_de_linha


class TesteQuebraDeLinha(TestCase):

    def test_frase_pequena(self):
        entrada = 'meu gato engasgou'
        saida_esperada = 'meu gato engasgou'
        saida = quebra_de_linha(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_outra_frase_pequena(self):
        entrada = 'o passaro voou'
        saida_esperada = 'o passaro voou'
        saida = quebra_de_linha(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_frase_que_quebra_direito(self):
        entrada = 'eu perdi a carteira andando na rua'
        saida_esperada = 'eu perdi a carteira\nandando na rua'
        saida = quebra_de_linha(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_frase_que_tambem_quebra_direito(self):
        entrada = 'eu perdi o mochilete andando na rua'
        saida_esperada = 'eu perdi o mochilete\nandando na rua'
        saida = quebra_de_linha(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_frase_grande_que_quebra_direito(self):
        entrada = 'eu perdi a carteira andando na rua, pois comia um sanduba do subway'
        saida_esperada = 'eu perdi a carteira\nandando na rua, pois\ncomia um sanduba do\nsubway'
        saida = quebra_de_linha(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_frase_pequena_que_quebra_palavra(self):
        entrada = 'tateando no escuro de repente sinto um'
        saida_esperada = 'tateando no escuro\nde repente sinto um'
        saida = quebra_de_linha(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_frase_grande_que_quebra_palavra(self):
        entrada = 'tateando no escuro de repente sinto um vento forte e extremamente gelado pelas costas'
        saida_esperada = 'tateando no escuro\nde repente sinto um\nvento forte e\nextremamente gelado\npelas costas'
        saida = quebra_de_linha(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_frase_com_palavras_grandes(self):
        entrada = 'tateandonoescuroderepentesintoumventoforte e extremamentegeladopelascostas'
        saida_esperada = 'tateandonoescuroderepentesintoumventoforte\ne\nextremamentegeladopelascostas'
        saida = quebra_de_linha(entrada)
        self.assertEqual(saida, saida_esperada)

    def test_frase_com_20_letras(self):
        entrada = 'abcdefghijklmnopqrst'
        saida_esperada = 'abcdefghijklmnopqrst'
        saida = quebra_de_linha(entrada)
        self.assertEqual(saida, saida_esperada)

    
if __name__ == '__main__':
    main()
