def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    flip_case = ''
    for letter in phrase:
        if letter.upper() == to_swap.upper():
            flip_case += letter.swapcase()
        else:
            flip_case += letter
    return flip_case
