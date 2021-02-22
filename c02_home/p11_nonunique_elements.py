# ---------------------------------------------------------------- #

# Non-unique Elements
#   Trim an array down to its non-unique elements
#   (Parsing, has-Hints)

# ---------------------------------------------------------------- #

# You are given a non-empty list of integers (X). For this task, you 
# should return a list consisting of only the non-unique elements in 
# this list. To do so you will need to remove all unique elements 
# (elements which are contained in a given list only once). 
# When solving this task, do not change the order of the list. 
# Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result 
# will be [1, 3, 1, 3].

# Input: A list of integers.
# Output: An iterable of integers.
# Precondition: 0 < len(data) < 1000

# How it is used: This mission will help you to understand how to 
# manipulate arrays, something that is the basis for solving more 
# complex tasks. The concept can be easily generalized for real 
# world tasks. For example: if you need to clarify statistics by 
# removing low frequency elements (noise).
# You can find out more about Python arrays in one of our articles 
# featuring lists, tuples, array.array and numpy.array.


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

def checkio(data: list) -> list:
    return [x for x in data if data.count(x) > 1]


def checkio_1(data: list) -> list:
    return list(filter(lambda x: data.count(x) > 1, data))


def checkio_2(data: list) -> list:
    #Your code here
    #It's main function. Don't remove this function
    #It's used for auto-testing and must return a result for check.  

    #replace this for solution
    new_data = []
    for num in data:
        if data.count(num) > 1:
            new_data.append(num)
    return new_data


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")

