# ---------------------------------------------------------------- #

# Sort Array by Element Frequency
#   Decreasing frequency order
#   (Iter, list)

# ---------------------------------------------------------------- #

# Sort the given iterable so that its elements end up in the decreasing 
# frequency order, that is, the number of times they appear in elements. 
# If two elements have the same frequency, they should end up in the 
# same order as the first appearance in the iterable.

# Input: Iterable
# Output: Iterable
# Precondition: elements can be ints or strings


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

def frequency_sort(items):
    return sorted(items, key = lambda x: (-items.count(x), items.index(x)))


def frequency_sort_1(items):
    # your code here
    items_info = []
    for item in list(set(items)):
        items_info.append([item, items.count(item), items.index(item)]) 

    items_sort = sorted(items_info, key = lambda x: [-x[1], x[2]])

    items_out = []
    for item in items_sort:
        items_out.extend([item[0]] * item[1])

    return items_out


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")

