# ---------------------------------------------------------------- #

# Acceptable Password IV
#   This mission will be unlocked after solving Acceptable Password III mission
#   (String, Bool)

# ---------------------------------------------------------------- #

# In this mission you need to create a password verification function.

# Those are the verification conditions:
#   the length should be bigger than 6;
#   should contain at least one digit, but it cannot consist of just digits;
#   having numbers or containing just numbers does not apply to the password longer than 9.

# Input: A string.
# Output: A bool.


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

def is_acceptable_password(password: str) -> bool:
    # your code here
    cnt = sum([ch.isdigit() for ch in password])
    return (cnt and cnt != len(password) and len(password) > 6) or len(password) > 9


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('short54') == True
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    assert is_acceptable_password('12345678910') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")

