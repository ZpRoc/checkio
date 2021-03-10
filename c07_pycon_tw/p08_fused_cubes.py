# ---------------------------------------------------------------- #

# Fused Cubes
#   Calculate the volume of objects that combines cubes
#   (Geometry, list, tuple, math)

# ---------------------------------------------------------------- #

# This is a mission to calculate the volume of objects that combines cubes.

# You are given a list of cube details (tuple of 4 integers: 
# X coordinate, Y coordinate, Z coordinate, edge length).
# - Each coordinate is the minimum value.
# - All edges parallel to the coordinate axes.

# If the cube share the part of another cube or touch with the face 
# of another cube, they are considered as one object. 
# You should return a list (or iterable) of the volumes of all objects.

# input: A list of tuples of 4 integers.
# output: A list (or iterable) of integers.


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

from typing import Tuple, List, Iterable
from functools import reduce


def fused_status(cube_1, cube_2) -> int:
    cube_s = sorted([cube_1, cube_2])
    cube_1 = cube_s[0]
    cube_2 = cube_s[1]

    cover = sum([cube_2[i] in range(cube_1[i] + 1, cube_1[i]+cube_1[3]) for i in range(3)])
    edge  = sum([cube_2[i] == cube_1[i] or cube_2[i] == cube_1[i]+cube_1[3] for i in range(3)])
    if cover == 3:                  # 'fused'
        return 3
    elif cover == 2 and edge == 1:  # 'touch with faces'
        return 2
    elif cover == 1 and edge == 2:
        return 1
    elif cover == 0 and edge == 3:  # 'touch with faces'
        return 2
    else:                           # 'touch with edges' OR 'touch with vertices' OR 'separated'
        return 1


def fused_cubes(cubes: List[Tuple[int]]) -> Iterable[int]:
    ### Group
    groups = []
    for cube in cubes:
        flg = False
        for g, group in enumerate(groups):
            for c in group:
                statue = fused_status(c, cube)
                if statue == 3 or statue == 2:
                    groups[g].append(cube)
                    flg = True
                    break
            if flg:
                break
        if not flg:
            groups.append([cube])

    ### Calculate volume
    volume = []

    ### Return
    return sorted(volume)


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

if __name__ == '__main__':
    assert sorted(fused_cubes([(0, 0, 0, 3), (1, 2, 2, 3)])) == [52], 'fused'
    assert sorted(fused_cubes([(0, 0, 0, 3), (1, 3, 2, 3)])) == [54], 'touch with faces'
    assert sorted(fused_cubes([(0, 0, 0, 3), (1, 3, 3, 3)])) == [27, 27], 'touch with edges'
    assert sorted(fused_cubes([(0, 0, 0, 3), (3, 3, 3, 3)])) == [27, 27], 'touch with vertices'
    assert sorted(fused_cubes([(0, 0, 0, 3), (3, 4, 3, 3)])) == [27, 27], 'separated'
    assert sorted(fused_cubes([(0, 0, 0, 3), (-2, -2, -2, 3)])) == [53], 'negative coordinates'
    assert sorted(fused_cubes([[-1,0,0,1],[1,0,0,1],[0,1,0,1],[0,-1,0,1],[0,0,1,1],[0,0,-1,1]])) == [1,1,1,1,1,1]
    assert sorted(fused_cubes([[0,0,0,1],[0,1,0,1],[0,2,0,1],[0,3,0,1],[0,5,0,1],[-1,4,0,1],[0,4,0,1],[1,4,0,1],[2,4,0,1],[3,4,0,1],[4,4,0,1],[5,4,0,1],[-1,6,0,1],[0,6,0,1],[1,6,0,1],[2,6,0,1],[3,6,0,1],[4,6,0,1],[5,6,0,1],[4,0,0,1],[4,1,0,1],[4,2,0,1],[4,3,0,1],[4,5,0,1],[2,5,0,1]])) == [25]
    print("Coding complete? Click 'Check' to earn cool rewards!")

