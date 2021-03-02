# ---------------------------------------------------------------- #

# Sum Consecutives
#   Sum strictly the identical and consecutive numbers in a given list of integers.
#   (List)

# ---------------------------------------------------------------- #

# You are given a list that contains solely integers (positive and negative). 
# Your job is to sum only the numbers that are identical and consecutive.

# Input: a list.
# Output: an iterable.


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

def sum_consecutives(a):
    # your code here
    if len(a) <= 1:       return a

    list_out = [a[0]]
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            list_out[-1] += a[i+1]
        else:
            list_out.append(a[i+1])
    return list_out


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

if __name__ == '__main__':
    print("Example:")
    print(list(sum_consecutives([1, 1, 1, 1])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(sum_consecutives([1, 1, 1, 1])) == [4]
    assert list(sum_consecutives([1, 1, 2, 2])) == [2, 4]
    assert list(sum_consecutives([1, 1, 2, 1])) == [2, 2, 1]
    assert list(sum_consecutives([3, 3, 3, 4, 4, 5, 6, 6])) == [9, 8, 5, 12]
    assert list(sum_consecutives([1])) == [1]
    assert list(sum_consecutives([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")

