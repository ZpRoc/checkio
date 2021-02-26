# ---------------------------------------------------------------- #

# Escape
#   Find out if a fly will escape from a jar or not.

# ---------------------------------------------------------------- #

# There is an open jar and a fly inside it. That fly is flying from 
# side to side frantically because it really wants to get away from 
# there. Your task is to estimate whether it will succeed in its 
# attempts (return True) or not (return False).

# So what do we got? The jar is represented by a rectangle in the 
# drawing above. It has width W and height H. The jar has a hole 
# of the size d. Our fly can escape through it. The hole is always 
# placed on the top of the jar and the jar is symmetrical. Point O 
# is the origin, the y-axis matches the jar's left side and the x-axis 
# matches the jar's bottom side. The wall thickness is negligible.

# Initial position of the fly is defined by x0 and y0, which are 
# assigned arbitrary. But it's guaranteed that the fly is inside the 
# jar by the time we start to observe it. In the very beginning the 
# fly is flying linearly, Vx and Vy are a horizontal and vertical 
# components of the velocity vector respectively. When the fly hits 
# a wall, it deflects from it and fly in the opposite direction 
# (like a billiard ball). The drawing above illustrates how it works. 
# Also, there's one tiny detail: after each collision the fly loses 
# 5% of its initial stamina, getting tired (velocity remains the same 
# though). So after 20 collisions the fly becomes completely exhausted. 
# The fly's size is negligible.

# Input: Two lists of integers:
#           the first contains jar's dims [W, H, d]
#           the second contains fly's characteristics [x0, y0, vx, vy]
# Output: True or False.
# Precondition: All dimensions are given in abstract units, velocities are given in units/sec.
#           W ∈ [100; 1000]
#           H ∈ [W; 4W]
#           d ∈ [0.1W; 0.8W]
#           x0 ∈ [0; W]
#           y0 ∈ [0; H]
#           vx ∈ (-2W; 2W)
#           vy ∈ (-2H; 2H)
#           V != 0


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

from typing import Tuple


FLY_FORMAT  = Tuple[float, float, float, float]


def reflect(fly: FLY_FORMAT, W, H, vx_d, vy_d) -> FLY_FORMAT:
    """ Solve the reflected coordinates and velocities. 
        fly    : [x0, y0, vx, vy]
        W      : 
        H      : 
        vx_d   : 
        vy_d   : 
        des_pct: 
    """
    ### Assign
    x_0, y_0, vx_0, vy_0 = fly

    ### Reflect
    # x_t = 0 or W
    if vx_0:
        px_x_t = W if vx_0 > 0 else 0
        px_y_t = (px_x_t - x_0) * vy_0 / vx_0 + y_0
    else:
        px_x_t = x_0
        px_y_t =  y_0

    if vy_0:      # y_t = 0 or H
        py_y_t = H if vy_0 > 0 else 0
        py_x_t = (py_y_t - y_0) * vx_0 / vy_0 + x_0
    else:
        py_x_t = x_0
        py_y_t = y_0

    # Velocity drop
    vx_t = (abs(vx_0) - vx_d) * (1 if vx_0 > 0 else -1)
    vy_t = (abs(vy_0) - vy_d) * (1 if vy_0 > 0 else -1)

    # Judge direction
    if vx_0 and px_y_t >= 0 and px_y_t <= H:
        x_t  = px_x_t
        y_t  = px_y_t
        vx_t = -vx_t
        vy_t =  vy_t

    if vy_0 and py_x_t >= 0 and py_x_t <= W:
        x_t  = py_x_t
        y_t  = py_y_t
        vx_t =  vx_t
        vy_t = -vy_t

    return [x_t, y_t, vx_t, vy_t]


def is_escape(fly: FLY_FORMAT, h, b1, b2) -> bool:
    ### Assign
    x_0, y_0, vx_0, vy_0 = fly

    ### is escape?
    if vy_0 <= 0:     return False

    y_t = h
    x_t = (y_t - y_0) * vx_0 / vy_0 + x_0 if vy_0 else x_0

    return True if x_t > b1 and x_t < b2 else False


def escape(jar, fly):
    ### Assign
    # Initial params
    W, H, D = jar
    x0, y0, vx, vy = fly

    # Border
    B1 = (W - D) / 2.0
    B2 = (W + D) / 2.0

    # Velocity drop
    vx_d = abs(vx) * 0.05
    vy_d = abs(vy) * 0.05

    ### Start reflect
    MAX_DEFLECT = 20
    while MAX_DEFLECT > 0:
        # is escape?
        if not is_escape([x0, y0, vx, vy], H, B1, B2):
            x0, y0, vx, vy = reflect([x0, y0, vx, vy], W, H, vx_d, vy_d)
        else:
            return True

        # Update
        MAX_DEFLECT -= 1
    else:
        return False


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

if __name__ == '__main__':
    print("Example:")
    print(escape([1000, 1000, 200], [0, 0, 100, 0]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert escape([1000, 1000, 200], [0, 0, 100, 0]) == False, "First"
    assert escape([1000, 1000, 200], [450, 50, 0, -100]) == True, "Second"
    assert escape([1000, 1000, 200], [450, 1000, 100, 0]) == False, "Third"
    assert escape([1000, 1000, 200], [250, 250, -10, -50]) == False, "Fourth"
    assert escape([1000, 2000, 200], [20, 35, 100, 175]) == True, "Fifth"
    print("Coding complete? Click 'Check' to earn cool rewards!")

