from lib.recipe_exercise import *

def test_contains_text():
    result = recipe_exercise("#TODO Buy milk")
    assert result == "This is one of your tasks"


def test_contains_text_NOT_in_caps():
    result = recipe_exercise("#todo Buy milk")
    assert result == "This is one of your tasks"
    
    
def test_does_NOT_contain_text():
    result = recipe_exercise("Buy milk")
    assert result == "This is NOT one of your tasks"
    
    
def test_contains_text_in_caps_but_no_hash():
    result = recipe_exercise("TODO Buy milk")
    assert result == "This is NOT one of your tasks"
    
    
def test_contains_text_in_lowercase_but_no_hash():
    result = recipe_exercise("todo Buy milk")
    assert result == "This is NOT one of your tasks"

