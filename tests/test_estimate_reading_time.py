from lib.estimate_reading_time import *

def test_estimate_reading_time():
    result = estimate_reading_time("Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day")
    assert result == "Estimated reading time: 1 minute"