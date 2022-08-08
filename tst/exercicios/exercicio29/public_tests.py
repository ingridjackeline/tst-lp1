import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global troca_vizinhos_condicional
        undertest = __import__(module)
        troca_vizinhos_condicional = getattr(undertest, 'troca_vizinhos_condicional', None)

    def test_simples(self):
        palavras = ["casa", "abacate", "boi", "casa", "jornal", "elo", "faca"]
        troca_vizinhos_condicional(palavras)
        assert palavras == ["abacate",  "casa", "boi", "casa", "elo", "jornal", "faca"]

    def test_2(self):
        palavras = ["elo", "diretor", "casa", "boi"]
        troca_vizinhos_condicional(palavras)
        assert palavras == ["diretor", "elo", "boi", "casa"]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
