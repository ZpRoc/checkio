# ---------------------------------------------------------------- #

# Cipher dict
#   Encrypt strings based on rules

# ---------------------------------------------------------------- #

# In this mission, you have to convert a plain text to a cipher dictionary 
# according to the next rules.
#   - Encode the plain text with utf-8.
#   - Take this value as a single hexadecimal number and convert it to a decimal number.
#   - Make a empty dictionary A.
#   - Add a data(key = value of each digit of decimal number, value = empty 
#     dictionary) to the appropriate dictionary.
#       - Initial dictionary is A.
#       - Change to a dictionary that was created earlier at the timing when the 
#         ascending order and descending order of the value of each digit of the 
#         decimal number are switched. (Change even if the same value continues.) 
#         Store from the upper digit. And find the ascending part first.
#         ex.)   decimal number == 1248854369653 → 1248 / 8543 / 69 / 653
#           - Change at the timing /.

# Input: A plain text as a string.
# Output: A cipher data as a dict.
# Precondition: The text contain only ASCII symbols.


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

def get_cipher(plain):
    # your code here
    return None


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

if __name__ == '__main__':
    print("Example:")
    print(get_cipher("hello"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert get_cipher("hello") == {4: {4: {8: {3: {7: {0: {4: {}, 7: {}}, 2: {2: {}}}, 8: {3: {}}}}}}}
    assert get_cipher("This is a plain text.") == {1: {3: {2: {1: {4: {7: {4: {1: {0: {}, 2: {}, 7: {}},4: {9: {}}, 8: {3: {}}},
                                                 6: {8: {1: {}, 4: {}, 9: {}}}}}, 9: {5: {5: {6: {1: {}, 4: {}}, 8: {}}}}}}}},
                                                 2: {6: {2: {8: {4: {9: {5: {2: {}, 8: {}}}}}}}}, 3: {2: {4: {1: {4: {8: {3: {0: {}, 
                                                 2: {}}}}}, 3: {5: {3: {5: {4: {}, 7: {}}}}}}}}}

    print("Coding complete? Click 'Check' to earn cool rewards!")

