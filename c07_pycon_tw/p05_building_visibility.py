# ---------------------------------------------------------------- #

# Building Visibility
#   "We built tall buildings, but we have not become any taller." — Dejan Stojanovic
#   (Matrix, numbers)

# ---------------------------------------------------------------- #

# For our future Robotropolis we need to help the city planners calculate 
# the way light reaches our fair city so as to limit the Urban Canyon effect. 
# To do this, you will need to define the visibility of buildings from the 
# southern edge of the base. You have been given a map of the buildings in 
# the complex as an aide for your planning.

# The map is an orthogonal projection of each of the buildings onto a 
# horizontal plane. It’s oriented on a rectangular coordinate system 
# so that the positive x-axis points east and the positive y-axis points 
# north. No two buildings in the map overlap or touch. Each of the buildings 
# have perfectly rectangular sides which are aligned from north to south 
# and east to west. The map is a list of buildings with each building presented 
# as a list with coordinates describing the south-west corner, and north-east 
# corner along with the height - [Xsw, Ysw, Xne, Yne, height]. We need to 
# determinate how many of the buildings are visible from the area just south 
# of the base (excluding the angle of vision, just using projection.)

# Input: Building coordinates and heights as a list of lists. The coordinates 
#        are integers. The heights are integers or floats.
# Output:The quantity of visible buildings as an integer.
# Precondition:
#       0 < len(buildings) < 10
#       all(all(0 ≤ x < 12 for x in row[:4]) for row in buildings)
#       all(0 < row[4] ≤ 20 for row in buildings)


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

def checkio(buildings):
    visible = 0
    for building in buildings:
        to_check = buildings.copy()
        to_check.remove(building)
        blocks = {i: False for i in range(building[0], building[2])}
        for x in range(building[0], building[2]):
            for check in to_check:
                if x in range(check[0], check[2]) and building[1] > check[1] and building[-1] <= check[-1]:
                    blocks[x] = True
                    continue
        if not all(blocks.values()):
            visible += 1
    return visible


def checkio_1(buildings):
    ### 该方法虽然复杂，但是可以兼容 [Xsw, Ysw, Xne, Yne] 坐标为浮点数的情况

    ### Initialization
    buildings = sorted(buildings, key = lambda x: [x[1], x[0]])
    b_visible = [buildings[0]]

    ### Loop
    for b in buildings[1:]:
        ### 筛选(高度小于等于已知建筑)且(位于已知建筑后面)的建筑的列
        cols = []
        for b_v in b_visible:
            cols = sorted(cols)
            if b[4] <= b_v[4] and b[1] >= b_v[3]:
                cols.append([b_v[0], b_v[2]])   
        
        ### 去除重复列操作
        cols = sorted(cols)
        i    = 1
        while i < len(cols):
            if cols[i][0] >= cols[i-1][0] and cols[i][0] <= cols[i-1][1]:
                cols[i-1][1] = max(cols[i][1], cols[i-1][1])
                cols.pop(i)
            else:
                i += 1

        ### 判断是否遮挡 [b[0], b[2]]
        is_visible = True
        for col in cols:
            if b[0] >= col[0] and b[2] <= col[1]:
                is_visible = False
                break

        ### 添加
        if is_visible:
            b_visible.append(b)

    ### return
    return len(b_visible)


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

if __name__ == '__main__':
    assert checkio([
        [1, 1, 4, 5, 3.5],
        [2, 6, 4, 8, 5],
        [5, 1, 9, 3, 6],
        [5, 5, 6, 6, 8],
        [7, 4, 10, 6, 4],
        [5, 7, 10, 8, 3]
    ]) == 5, "First"
    assert checkio([
        [1, 1, 11, 2, 2],
        [2, 3, 10, 4, 1],
        [3, 5, 9, 6, 3],
        [4, 7, 8, 8, 2]
    ]) == 2, "Second"
    assert checkio([
        [1, 1, 3, 3, 6],
        [5, 1, 7, 3, 6],
        [9, 1, 11, 3, 6],
        [1, 4, 3, 6, 6],
        [5, 4, 7, 6, 6],
        [9, 4, 11, 6, 6],
        [1, 7, 11, 8, 3.25]
    ]) == 4, "Third"
    assert checkio([
        [0, 0, 1, 1, 10]
    ]) == 1, "Alone"
    assert checkio([
        [2, 2, 3, 3, 4],
        [2, 5, 3, 6, 4]
    ]) == 1, "Shadow"
    assert checkio([
        [1,1,3,3,20],
        [3,4,5,6,20],
        [5,1,7,3,20],
        [1,7,7,9,20]
    ]) == 3

