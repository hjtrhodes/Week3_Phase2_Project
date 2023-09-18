# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._
# As a user
# So that I can improve my grammar
# I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def sentence_checker(sentence_string):
    #check that the sentence starts with a capital letter and ends with a full stop
    #parameters: a string containing a sentence 
    #Returns: 
    #   True: a string "This sentence is correctly punctuated!"
    #   False: a string "This sentence is NOT correctly punctuated!"
    #Side Effects: None
    pass

```



## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Given a string with capital but no full stop
it returns "This sentence is NOT correctly punctuated!"
"""

sentence_checker("This is a bad sentence") => ["This sentence is NOT correctly punctuated!"]

"""
Given a string with no capital but a full stop
it returns "This sentence is NOT correctly punctuated!"
"""
sentence_checker("this is a bad sentence.") => ["This sentence is NOT correctly punctuated!"]

"""
Given a string with no capital and no full stop
it returns "This sentence is NOT correctly punctuated!"
"""
sentence_checker("this is a bad sentence") => ["This sentence is NOT correctly punctuated!"]

"""
Given a string with a capital and a full stop
it returns "This sentence is correctly punctuated!"
"""
sentence_checker("This is a good sentence.") => ["This sentence is correctly punctuated!"]


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
