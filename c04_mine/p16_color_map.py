# ---------------------------------------------------------------- #

# Color Map
#   "Everything is related to everything else, but near things are 
#   more related than distant things." -- Tobler Waldo
#   (Numbers, math)

# ---------------------------------------------------------------- #

# In mathematics the four color theorem, or the four color map theorem, 
# states that: when given any separation of a plane into contiguous regions 
# and producing a figure called a map, no more than four colors are 
# required to color the regions of the map so that no two adjacent 
# regions have the same color. Two regions are called adjacent if they 
# share a common boundary that is not a corner, where corners are the 
# points shared by three or more regions. For our model we will use a 
# grid with square cells.

# You are given a regional map as a grid (matrix). There are N countries 
# located on this map. Each country has a number from 0 to N-1. Two cells 
# are adjacent if they have a common edge. Each country has one or more 
# cells that are connected. Thus you can move between any cells of the 
# country X just using for this adjacent cells.

# Each cell is marked by the number of its designated country.

# You should "color" a map with 4 colors. All of the cells comprising 
# one country should be one color. Adjacent cells of various countries 
# should not have the same color.

# The result should be represented as a sequence of numbers 1,2,3 or 4. 
# Each element shows the color of its country matching the index. For 
# example, the 0th element shows the color of country 0. So the result 
# should have N elements.

# Input: A map of region as a tuple of tuples with integers.
# Output: The color sequence as a tuple/list of integer.
# Precondition: 0 < len(region) ≤ 10
#               all(0 < len(row) ≤ 10 and len(row) == len(region[0]) for row in region)
#               One country cells are connected.
#               Country numbers are sequence from 0 to N-1.


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

def color_map(region):
    return [1, 1]


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    NEIGHS = ((-1, 0), (1, 0), (0, 1), (0, -1))
    COLORS = (1, 2, 3, 4)
    ERROR_NOT_FOUND = "Didn't find a color for the country {}"
    ERROR_WRONG_COLOR = "I don't know about the color {}"

    def checker(func, region):
        user_result = func(region)
        if not isinstance(user_result, (tuple, list)):
            print("The result must be a tuple or a list")
            return False
        country_set = set()
        for i, row in enumerate(region):
            for j, cell in enumerate(row):
                country_set.add(cell)
                neighbours = []
                if j < len(row) - 1:
                    neighbours.append(region[i][j + 1])
                if i < len(region) - 1:
                    neighbours.append(region[i + 1][j])
                try:
                    cell_color = user_result[cell]
                except IndexError:
                    print(ERROR_NOT_FOUND.format(cell))
                    return False
                if cell_color not in COLORS:
                    print(ERROR_WRONG_COLOR.format(cell_color))
                    return False
                for n in neighbours:
                    try:
                        n_color = user_result[n]
                    except IndexError:
                        print(ERROR_NOT_FOUND.format(n))
                        return False
                    if cell != n and cell_color == n_color:
                        print("Same color neighbours.")
                        return False
        if len(country_set) != len(user_result):
            print("Excess colors in the result")
            return False
        return True
    assert checker(color_map, (
        (0, 0, 0),
        (0, 1, 1),
        (0, 0, 2),
    )), "Small"
    assert checker(color_map, (
        (0, 0, 2, 3),
        (0, 1, 2, 3),
        (0, 1, 1, 3),
        (0, 0, 0, 0),
    )), "4X4"
    assert checker(color_map, (
        (1, 1, 1, 2, 1, 1),
        (1, 1, 1, 1, 1, 1),
        (1, 1, 0, 1, 1, 1),
        (1, 0, 0, 0, 1, 1),
        (1, 1, 0, 4, 3, 1),
        (1, 1, 1, 3, 3, 3),
        (1, 1, 1, 1, 3, 5),
    )), "6 pack"

