import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global palavras_com_caractere
        undertest = __import__(module)
        palavras_com_caractere = getattr(undertest, 'palavras_com_caractere', None)

    def test_basico_1(self):
        assert palavras_com_caractere(["casa", "carro", "teste"], "x") == 0

    def test_basico_2(self):
        assert palavras_com_caractere(["casa", "carro", "teste"], "r") == 1

    def test_basico_3(self):
        assert palavras_com_caractere(["casa", "carro", "teste"], "a") == 2
        
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
