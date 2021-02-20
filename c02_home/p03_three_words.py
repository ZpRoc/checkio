# ---------------------------------------------------------------- #

# Three Words
#   How to discern words and numbers.
#   (String, has-Hint, sparsing)

# ---------------------------------------------------------------- #

# Let's teach the Robots to distinguish words and numbers.

# You are given a string with words and numbers separated by 
# whitespaces (one space). The words contains only letters. 
# You should check if the string contains three words in succession. 
# For example, the string "start 5 one two three 7 end" contains 
# three words in succession.

# Input: A string with words.
# Output: The answer as a boolean.
# Precondition: The input contains words and/or numbers. 
#               There are no mixed words (letters and digits combined).
#               0 < len(words) < 100


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

def checkio(words: str) -> bool:
    val = [i.isdigit() for i in words.split()]
    return 'False, False, False' in ''.join(str(val))


def checkio_1(words: str) -> bool:
    cnt = 0
    for word in words.split(' '):
        cnt = cnt + 1 if not word.isdigit() else 0
        if cnt > 2:
            return True  
    return False


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))
    
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

