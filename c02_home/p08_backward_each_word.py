# ---------------------------------------------------------------- #

# Backward Each Word
#   Reverse every word in a given line
#   (String)

# ---------------------------------------------------------------- #

# In a given string you should reverse every word, but the words 
# should stay in their places.

# Input: A string.
# Output: A string.
# Precondition: The line consists only from alphabetical symbols and spaces.


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

def backward_string_by_word(text: str) -> str:
    # your code here
    return ' '.join(x[::-1] for x in text.split(' '))


def backward_string_by_word_1(text: str) -> str:
    # your code here
    str_out = ''
    for word in text.split(' '):
        str_out += word[::-1] + ' '
    return str_out[0:-1]


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")

