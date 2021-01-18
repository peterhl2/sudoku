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

    # returns whether the number doesn't exist in the Box
    def checkValidBox(self, num, i, j):
        box = self.grid[i / 3][j / 3]
        for a in range(3):
            for b in range(3):
                if box[a][b] == num:
                    return False

        return True

# 3x3 grid of Boxes for the game board
class Board:
    def __init__():
        self.grid = [
            [Box(), Box(), Box()],
            [Box(), Box(), Box()],
            [Box(), Box(), Box()]
        ]

    # TODO: Write this function, takes user input and create a gameboard
    def fillBoard(self, numbers):
        return

    # TODO: Write this function, prints the entire game board
    def print():
        print("Printing Game Board")
        print("--------------------------------")
        print("--------------------------------")
        return

    # TODO: Write this function, solve
    def solve():
        return

    def get(self, i, j):
        boardX = i / 3
        boardY = j / 3
        boxX = i % 3
        boxY = j % 3
        return self.grid[boardX][boardY].get(boxX, boxY)

    def getRow(self, i):
        box0 = self.grid[i/3][0]
        box1 = self.grid[i/3][1]
        box2 = self.grid[i/3][2]
        row = [
            box0[i%3][0], box0[i%3][1], box0[i%3][2],
            box1[i%3][0], box1[i%3][1], box1[i%3][2],
            box2[i%3][0], box2[i%3][1], box2[i%3][2]
        ]
        return row

    def getColumn(self, j):
        box0 = self.grid[0][j/3]
        box1 = self.grid[1][j/3]
        box2 = self.grid[2][j/3]
        col = [
            box0[0][j%3], box0[1][j%3], box0[2][j%3],
            box1[0][j%3], box1[1][j%3], box1[2][j%3],
            box2[0][j%3], box2[1][j%3], box2[2][j%3]
        ]
        return col

    # returns whether the number doesn't exist in the Row
    def checkValidRow(num, i):
        return not num in getRow(i)

    # returns whether the number doesn't exist in the Column
    def checkValidCol(num, j):
        return not col in getCol(j)

def createBlankBoard():
    return Board()

def createUserBoard():
    board = Board()
    numbers = input("Enter a list of values")
    board.fillBoard(numbers)
    return board

gameBoard = createUserBoard()

solve(gameBoard)

gameBoard.print()
