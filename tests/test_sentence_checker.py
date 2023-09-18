from lib.sentence_checker import *

def test_no_capital():
    result = sentence_checker("this is a bad sentence.")
    assert result == "This sentence is NOT correctly punctuated!"

def test_no_full_stop():
    result = sentence_checker("This is a bad sentence")
    assert result == "This sentence is NOT correctly punctuated!"

def test_no_capital_no_full_stop():
    result = sentence_checker("this is a bad sentence")
    assert result == "This sentence is NOT correctly punctuated!"

def test_correct_sentence():
    result = sentence_checker("This is a good sentence.")
    assert result == "This sentence is correctly punctuated!"