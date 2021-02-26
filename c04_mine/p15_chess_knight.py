# ---------------------------------------------------------------- #

# Chess Knight
#   Find all of the chessboard cells to which the Knight can move.
#   (Games, list, path, finding)

# ---------------------------------------------------------------- #

# Your friend loves chess very much, but he's not a strong player. 
# You can help him by using your programming skills.
# If this mission is too simple for you, try another one from this 
# set - The shortest Knight's path.

# Your task is to write a function that can find all of the chessboard 
# cells to which the Knight can move. The input data will consist of a 
# start cell and the amount of moves that the Knight will make. There 
# is only one figure on the board - your Knight.
# If the same cell appears more than once - do not add it again. You 
# should return the list of all of the possible cells and sort them 
# as follows: in alphabetical order (from 'a' to 'h') and in ascending 
# order (from 'a1' to 'a8' and so on).

# Input: A start cell, the number of moves.
# Output: A list of all of the possible cells.
# Precondition: 1 <= the number of moves <= 2


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

ALL_POS = [chr(x)+str(y) for x in range(ord('a'), ord('h') + 1) for y in range(1, 9)]
OFFSETS = [[x, y] for x in [-1, 1, -2, 2] for y in [-1, 1, -2, 2] if abs(x) != abs(y)]


def chess_knight(start, moves):
    #replace this for solution
    out   = []
    start = [start]
    for _ in range(moves):
        stop = []
        for s in start:
            stop.extend([chr(ord(s[0])+o[0])+str(int(s[1])+o[1]) for o in OFFSETS])
        out.extend(set([s for s in stop if s in ALL_POS]))
        start = out
    return sorted(out, key = lambda x: [x[0], x[1]])


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

if __name__ == '__main__':
    print("Example:")
    print(chess_knight('a1', 1))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert chess_knight('a1', 1) == ['b3', 'c2']
    assert chess_knight('h8', 2) == ['d6', 'd8', 'e5', 'e7', 'f4', 'f7', 'f8', 'g5', 'g6', 'h4', 'h6', 'h8']
    print("Coding complete? Click 'Check' to earn cool rewards!")

