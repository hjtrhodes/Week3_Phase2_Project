# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

As a user So that I can keep track of my tasks I want to check if a text includes the string #TODO

## 2. Design the Function Signature

def includes_to_do(text_string):
    Purpose: Checks if a text string includes the letters #TODO
    Parameters: Argument is a string of mixed words
    Returns: - if True 'This is one of your tasks'
             - if false: This is NOT one of your tasks'

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given 
It returns 
"""
includes_to_do("hello WORLD") => ["WORLD"]

"""
Given a string containing #TODO
It returns: This is one of your tasks'
"""
includes_to_do("#TODO Buy milk") => ["This is one of your tasks"]

"""
Given a string containing #TODO but NOT in caps
It returns: This is one of your tasks'
"""
includes_to_do("#todo Buy milk") => ["This is one of your tasks"]

"""
Given a string NOT containing #TODO
It returns: This is NOT one of your tasks'
"""
includes_to_do("Buy milk") => ["This is NOT one of your tasks"]

"""
Given a string containing #TODO but with no #
It returns: This is NOT one of your tasks'
"""
includes_to_do("todo Buy milk") => ["This is NOT one of your tasks"]
includes_to_do("TODO Buy milk") => ["This is NOT one of your tasks"]






```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
