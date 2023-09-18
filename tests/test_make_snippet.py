from lib.make_snippet import *

def test_make_snippet():
    result = make_snippet("hello we are pair programming for the first time")
    assert result == "hello we are pair programming..."