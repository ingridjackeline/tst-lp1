import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global remove_multiplos
        undertest = __import__(module)
        remove_multiplos = getattr(undertest, 'remove_multiplos', None)

    def test_exemplo_1(self):
        numeros = [2, 4, 6, 5, 7, 3, 10, 1]
        assert remove_multiplos(2, numeros) == 4
        assert numeros == [5, 7, 3, 1]

    def test_exemplo_2(self):
        numeros = [2, 4, 6, 5, 7, 3, 10, 1]
        assert remove_multiplos(3, numeros) == 2
        assert numeros == [2, 4, 5, 7, 10, 1]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
