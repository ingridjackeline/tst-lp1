import unittest
import sys

module = sys.argv[-1].split(".py")[0]


class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global remove_repetidos
        undertest = __import__(module)
        remove_repetidos = getattr(undertest, 'remove_repetidos', None)

    def test_example(self):
        l = [1, 1, 2, 2, 5, 1]
        assert remove_repetidos(l) == None
        assert l == [1,2,5]

    def test_exemplo2(self):
        l = [1, 2, 1, 2, 1, 1]
        assert remove_repetidos(l) == None
        assert l == [1, 2]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
