# ---------------------------------------------------------------- #

# Acceptable Password III
#   This mission will be unlocked after solving Acceptable Password II mission
#   (String, Bool)

# ---------------------------------------------------------------- #

# In this mission you need to create a password verification function.

# Those are the verification conditions:
#   the length should be bigger than 6;
#   should contain at least one digit, but cannot consist of just digits.

# Input: A string.
# Output: A bool.


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

def is_acceptable_password(password: str) -> bool:
    # your code here
    cnt = sum([ch.isdigit() for ch in password])
    return cnt and cnt != len(password) and len(password) > 6


def is_acceptable_password_2(password: str) -> bool:
    return True if len(password) > 6 and len(set([symb.isdigit() for symb in password])) == 2 else False


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == False
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")

