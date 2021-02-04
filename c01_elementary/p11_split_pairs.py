# ---------------------------------------------------------------- #

# Split Pairs
#   Split the string into pairs of two characters.
#   (list)

# ---------------------------------------------------------------- #

# Split the string into pairs of two characters. 
# If the string contains an odd number of characters, then the 
# missing second character of the final pair should be replaced 
# with an underscore ('_').

# Input: A string.
# Output: An iterable of strings.
# Precondition: 0<=len(str)<=100


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

def split_pairs(a):
    # your code here
    a = a + '_' if len(a) % 2 else a

    b = []
    for i in range(0, len(a), 2):
        b.append(a[i:i+2])

    return b


def split_pairs_1(a):
    from textwrap import wrap

    a = a + '_' if len(a) % 2 else a
    return wrap(a, 2)


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")

