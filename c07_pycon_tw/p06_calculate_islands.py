# ---------------------------------------------------------------- #

# Calculate Islands
#   Help the robots calculate the landmass of their newly discovered island chain.
#   (Matrix, geometry)

# ---------------------------------------------------------------- #

# The Robots have found a chain of islands in the middle of the Ocean. 
# They would like to explore these islands and have asked for your help 
# calculating the areas of each island. They have given you a map of the 
# territory. The map is a 2D array, where 0 is water, 1 is land. An island 
# is a group of land cells surround by water. Cells are connected by their 
# edges and corners. You should calculate the areas for each of the islands 
# and return a list of sizes (quantity of cells) in ascending order. 
# All of the cells outside the map are considered to be water.

# Input: A map as a list of lists with 1 or 0.
# Output: The sizes of island as a list of integers.
# Precondition: 0 < len(land_map) < 10
#               all(len(land_map[0]) == len(row) for row in land_map)
#               any(any(row) for row in land_map)


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

from typing import List
import numpy as np


def checkio(land_map: List[List[int]]) -> List[int]:
    ### Initialization
    MAP      = np.array(land_map, dtype=np.uint8)
    FLG      = np.zeros_like(MAP, dtype=np.uint8)
    ROW, COL = np.shape(MAP)
    CNT = 0

    ### Judge
    for r in range(ROW):
        for c in range(COL):
            if MAP[r, c] == 1:
                ### 该位置周围是否已经被标记：是 跟从标记，否 新标记
                flg_slt = FLG[max(r-1, 0):min(r+2, ROW), max(c-1, 0):min(c+2, COL)]
                if np.sum(flg_slt) == 0:
                    CNT       = CNT + 1
                    FLG[r, c] = CNT
                else:
                    FLG[r, c] = np.max(flg_slt)

    ### Concat
    for r in range(ROW):
        for c in range(COL):
            if FLG[r, c] != 0:
                ### 该位置周围是否被标记为相同编号：是 pass，否 用小的编号代替大的编号
                flg_slt = FLG[max(r-1, 0):min(r+2, ROW), max(c-1, 0):min(c+2, COL)]
                if np.sum(flg_slt==0) + np.sum(flg_slt==FLG[r, c]) != np.size(flg_slt):
                    tmp = np.extract(((flg_slt != 0) & (flg_slt != FLG[r, c])), flg_slt)
                    FLG = np.where(FLG==tmp[0], FLG[r, c], FLG)

    ### Count & Sort
    aera_list = sorted([np.sum(FLG==cnt+1) for cnt in range(CNT)])
    return aera_list[aera_list.count(0):]


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

if __name__ == '__main__':
    print("Example:")
    print(checkio([[0, 0, 0, 0, 0],
                   [0, 0, 1, 1, 0],
                   [0, 0, 0, 1, 0],
                   [0, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0]]))

    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0]]) == [5], "2nd example"
    assert checkio([[0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"
    print("Coding complete? Click 'Check' to earn cool rewards!")

