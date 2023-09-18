# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._
# As a user so that I can manage my time I want to see an estimate of reading time for a text, assuming that I can read 200 words per minute

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def estimate_reading_time(string):
    # counts the words in the text
    # Parameters: A string containing words
    # Returns: A string "estimated reading time: x number of minutes"
    # Side Effects: None
    pass

```



## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Given a string with 200 words
It returns an estimated time of 1 minute
"""
estimate_reading_time("Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day") => ["Estimated reading time: 1 minute"]

"""
Given a string with 400 words
It returns an estimated time of 2 minutes
"""
estimate_reading_time("Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day") => ["Estimated reading time: 2 minutes"]

"""
Given a string with 300 words
It returns a rounded up estimate of 2 minutes
"""
estimate_reading_time("Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day") => ["Estimated reading time: 2 minutes"]

"""
Given a string with no words
It returns an error
"""
estimate_reading_time("") => ["Cannot estimate reading time"]

```
# EXAMPLE
```python
"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
extract_uppercase("hello WORLD") => ["WORLD"]

"""
Given two uppercase words
It returns a list with both words
"""
extract_uppercase("HELLO WORLD") => ["HELLO", "WORLD"]

"""
Given two lowercase words
It returns an empty list
"""
extract_uppercase("hello world") => []

"""
Given a lower and a mixed case word
It returns an empty list
"""
extract_uppercase("hello WoRLD") => []

"""
Given a lowercase word and an uppercase word with an exclamation mark
It returns a list with the uppercase word, no exclamation mark
"""
extract_uppercase("hello WORLD!") => ["WORLD"]

"""
Given an empty string
It returns an empty list
"""
extract_uppercase("") => []

"""
Given a None value
It throws an error
"""
extract_uppercase(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

```

Ensure all test function names are unique, otherwise pytest will ignore them!


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
