# 3x3 grid of unique numbers from 1-9
class Box:
    def __init__():
        self.grid = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]

    def get(self, i, j):
        return self.grid[i][j]

# 3x3 grid of Boxes for the game board
class Board:
    def __init__():
        self.grid = [
            [Box(), Box(), Box()],
            [Box(), Box(), Box()],
            [Box(), Box(), Box()]
        ]

    def get(self, i, j):
        boardX = i / 3
        boardY = j / 3
        boxX = i % 3
        boxY = j % 3
        return self.grid[boardX][boardY].get(boxX, boxY)

    # returns whether the number doesn't exist in the Row
    def checkValidRow(num, i, j):
        return 0

    # returns whether the number doesn't exist in the Column
    def checkValidCol(num, i, j):
        return 0

    # returns whether the number doesn't exist in the Box
    def checkValidBox(num, i, j):
        return 0
