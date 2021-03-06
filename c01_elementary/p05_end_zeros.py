# ---------------------------------------------------------------- #

# End Zeros
#   How many zeros are at the end?
#   (string)

# ---------------------------------------------------------------- #

# Try to find out how many zeros a given number has at the end.

# Input: A positive Int
# Output: An Int.


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

def end_zeros(num: int) -> int:
    # your code here
    n = str(num)
    return len(n) - len(n.strip('0'))


def end_zeros_1(num: int) -> int:
    cnt = len(str(num))
    while cnt > 0:
        if num % (10**cnt) == 0:
            break
        else:
            cnt = cnt - 1
    return cnt


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")

