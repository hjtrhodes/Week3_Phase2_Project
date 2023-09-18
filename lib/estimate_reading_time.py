def estimate_reading_time(text):
    word_count = len(text.split())
    reading_time = word_count/200
    rounded_reading_time = round(reading_time)
    if word_count < 200 and word_count > 0:
        return "Estimated reading time: less than 1 minute"
    if rounded_reading_time == 1:
        return f"Estimated reading time: {rounded_reading_time} minute"
    if rounded_reading_time > 1:
        return f"Estimated reading time: {rounded_reading_time} minutes"
    else:
        return "Cannnot estimate reading time"
    

    #need output for greater than 1 minute to be minutes
    #check that round is working the way we want

print(estimate_reading_time("Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day Hello world how are you doing on this fine day"))
