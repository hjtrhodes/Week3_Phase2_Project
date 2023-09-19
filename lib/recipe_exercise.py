def recipe_exercise(string):
    search_text = '#TODO'
    if search_text in string.upper():
        return "This is one of your tasks"
    else:
        return "This is NOT one of your tasks"