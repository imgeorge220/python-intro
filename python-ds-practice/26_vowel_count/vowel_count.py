def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!')
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    vowels = {"a", "e", "i", "o", "u"}
    phrase = phrase.lower()
    results = {}
    for letter in phrase:
        if letter in vowels:
            results[letter] = 1 if (results.get(letter, 0) == 0) else results[letter] + 1

    return results
