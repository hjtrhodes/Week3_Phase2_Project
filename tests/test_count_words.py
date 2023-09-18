from lib.count_words import *

def test_count_words():
    result = count_words("hello we are pair programming for the first time")
    assert result == 9