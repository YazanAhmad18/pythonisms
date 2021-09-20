from pythonic import __version__
from pythonic.pythonic import *


def test_version():
    assert __version__ == '0.1.0'

def test_factors_1():
    actual = factors_one(200)
    expected = [1, 2, 4, 5, 8, 10, 20, 25, 40, 50,100,200]
    assert actual == expected


