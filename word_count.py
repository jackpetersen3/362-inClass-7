def wordCount():
    string = raw_input("Enter a sentence: ")
    if not string:
        return 0
    else:
        words = string.split()
        num_words = len(words)
        return num_words
    
        



