def sentence_checker(sentence_string):
    correct_or_incorrect = ["This sentence is correctly punctuated!", "This sentence is NOT correctly punctuated!"]
    if sentence_string[0].isupper() == True and sentence_string[-1] == '.':
        return correct_or_incorrect[0]
    else: 
        return correct_or_incorrect[1]