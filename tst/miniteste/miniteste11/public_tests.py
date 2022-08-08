import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global seleciona_perfeitos
        undertest = __import__(module)
        seleciona_perfeitos = getattr(undertest, 'seleciona_perfeitos', None)

    def test_1_publico(self):
        lista = [3, 6, 9, 12, 15, 18, 19, 21, 28]
        assert seleciona_perfeitos(lista) == [6, 28]
        assert lista == [3, 6, 9, 12, 15, 18, 19, 21, 28]


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
