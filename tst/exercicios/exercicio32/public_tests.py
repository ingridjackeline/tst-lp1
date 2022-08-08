import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global intersecao_listas
        undertest = __import__(module)
        intersecao_listas = getattr(undertest, 'intersecao_listas', None)

    def test_exemplo(self):
        lista1 = [2, 1, 3, 4]
        lista2 = [2]
        intersecao_listas(lista1, lista2)
        assert lista1 == [2]
    
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
