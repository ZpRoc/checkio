# ---------------------------------------------------------------- #

# The Greatest Common Divisor
#   Add short description
#   (Math, numbers)

# ---------------------------------------------------------------- #

# The greatest common divisor (GCD), also known as the greatest common 
# factor of two or more integers (at least one of which is not zero), 
# is the largest positive integer that divides a number without a remainder. 
# For example, the GCD of 8 and 12 is 4.

# You are given an arbitrary number of positive integers. You should find 
# the greatest common divisor for these numbers.

# Input: An arbitrary number of positive integers.
# Output: The greatest common divisor as an integer.
# Precondition:
#           1 < len(args) ≤ 10
#           all(0 < x ≤ 2 ** 32 for x in args)


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

def greatest_common_divisor(*args: int) -> int:
    nums = sorted(set(args))
    while True:
        ### Remove 0
        nums = {num for num in nums if num}
        if len(nums) == 1:      return nums.pop()

        ### 辗转相除法
        nums = sorted({num % min(nums) if num != min(nums) else num for num in nums})


def greatest_common_divisor_1(*args: int) -> int:
    # 可以定义一个函数 f，求解两个数的最大公约数
    # 利用 reduce 进行迭代调用，即 reduce(f, args)
    return 1


def greatest_common_divisor_2(*args: int) -> int:
    # your code here
    for num in range(min(args), 0, -1):
        if sum([x % num for x in args]) == 0:
            return num
    return 1


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

if __name__ == '__main__':
    print("Example:")
    print(greatest_common_divisor(6, 4))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert greatest_common_divisor(2167650657, 1496767446, 2685881265, 452884638, 2222724963) == 3
    assert greatest_common_divisor(6, 4) == 2
    assert greatest_common_divisor(2, 4, 8) == 2
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1
    assert greatest_common_divisor(3, 9, 3, 9) == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")

