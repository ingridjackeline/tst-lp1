import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global split
        undertest = __import__(module)
        split = getattr(undertest, 'split', None)

    def test_simples(self):
        assert split('um exemplo', ' ') == ['um','exemplo']
        
    def test_exemplo(self):
        assert split('um exemplo maior',' ') == ['um','exemplo','maior']

    def test_exemplo(self):
        assert split('duas,,palavras',',') == ['duas','palavras']

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
