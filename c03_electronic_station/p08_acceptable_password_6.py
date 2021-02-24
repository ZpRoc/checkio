# ---------------------------------------------------------------- #

# Acceptable Password VI
#   This mission will be unlocked after solving Acceptable Password V mission
#   (String, Bool)

# ---------------------------------------------------------------- #

# In this mission you need to create a password verification function.

# Those are the verification conditions:
#   the length should be bigger than 6;
#   should contain at least one digit, but it cannot consist of just digits;
#   having numbers or containing just numbers does not apply to the password longer than 9.
#   a string should not contain the word "password" in any case;
#   should contain 3 different letters (or digits) even if it is longer than 10

# Input: A string.
# Output: A bool.


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

def is_acceptable_password(password):
    # your code here
    cnt  = sum([ch.isdigit() for ch in password])
    pw   = 'password' not in password.lower()
    diff = len(set([ch for ch in password])) > 2
    return ((cnt and cnt != len(password) and len(password) > 6) or len(password) > 9) and pw and diff


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
    assert is_acceptable_password('password12345') == False
    assert is_acceptable_password('PASSWORD12345') == False
    assert is_acceptable_password('pass1234word') == True
    assert is_acceptable_password('aaaaaa1') == False
    assert is_acceptable_password('aaaaaabbbbb') == False
    assert is_acceptable_password('aaaaaabb1') == True
    assert is_acceptable_password('abc1') == False
    assert is_acceptable_password('abbcc12') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")

