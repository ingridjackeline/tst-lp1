import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
get_frequencia = getattr(undertest, 'get_frequencia', None)

class PublicTests(unittest.TestCase):

    def test_exemplo(self):
        assert get_frequencia(['b','b','c','b', 'a']) == [3,1,1]
     
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
