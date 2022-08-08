import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global filtra_altera_lista
        undertest = __import__(module)
        filtra_altera_lista = getattr(undertest, 'filtra_altera_lista', None)

    def test_basico(self):
        seq = [0,1,2,3,4,5,6]
        filtra_altera_lista(2, seq)
        assert seq == [0, 2, 4 ,6]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
