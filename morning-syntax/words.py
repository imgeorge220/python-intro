def print_upper_words(lst, valid_letters):
    '''prints words in list after converting to uppercase'''

    for letter in valid_letters:
        valid_letters.remove(letter)
        valid_letters.add(letter.upper())

    for word in lst:
        word_upper = word.upper()
        if word_upper[0] in valid_letters:
            print(word_upper)
    
print_upper_words(["hello", "hey", "GOODBYE", "yo", "yes"], {"g", "y"})