# 3x3 grid of unique numbers from 1-9
class Box:
    def __init__(self):
        self.grid = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]

    def get(self, i, j):
        return self.grid[i][j]

    def set(self, i, j, num):
        self.grid[i][j] = num
        return

    # returns whether the number doesn't exist in the Box
    def checkValidBox(self, num, i, j):
        box = self.grid[i // 3][j // 3]
        for a in range(3):
            for b in range(3):
                if box[a][b] == num:
                    return False

        return True

# 3x3 grid of Boxes for the game board
class Board:
    def __init__(self):
        self.grid = [
            [Box(), Box(), Box()],
            [Box(), Box(), Box()],
            [Box(), Box(), Box()]
        ]

    # TODO: Write this function, takes user input and create a gameboard
    def fillBoard(self, numbersList):
        numbersList = numbersList.split(" ")
        numbers = []
        for i in range(81):
            if i < len(numbersList):
                numbers.append(int(numbersList[i]))
            else:
                numbers.append(0)
        print(numbers)
        for i in range(9):
            for j in range(9):
                self.set(i, j, numbers[i*9 + j])
        return

    # TODO: Write this function, prints the entire game board
    def print(self):
        print("Printing Game Board")
        print("-------------------------")
        self.printRow(0)
        self.printRow(1)
        self.printRow(2)
        print("-------------------------")
        self.printRow(3)
        self.printRow(4)
        self.printRow(5)
        print("-------------------------")
        self.printRow(6)
        self.printRow(7)
        self.printRow(8)
        print("-------------------------")
        return

    def printRow(self, i):
        fullRow = "| {} {} {} | {} {} {} | {} {} {} |"
        print(fullRow.format(self.get(i,0), self.get(i,1), self.get(i,2),
                             self.get(i,3), self.get(i,4), self.get(i,5),
                             self.get(i,6), self.get(i,7), self.get(i,8)))
        return

    # TODO: Write this function, solve
    def solve(self):
        return

    def set(self, i, j, num):
        boardX = i // 3
        boardY = j // 3
        boxX = i % 3
        boxY = j % 3
        box = self.grid[boardX][boardY]
        box.set(boxX, boxY, num)
        return

    def get(self, i, j):
        boardX = i // 3
        boardY = j // 3
        boxX = i % 3
        boxY = j % 3
        return self.grid[boardX][boardY].get(boxX, boxY)

    def getRow(self, i):
        box0 = self.grid[i//3][0]
        box1 = self.grid[i//3][1]
        box2 = self.grid[i//3][2]
        row = [
            box0[i%3][0], box0[i%3][1], box0[i%3][2],
            box1[i%3][0], box1[i%3][1], box1[i%3][2],
            box2[i%3][0], box2[i%3][1], box2[i%3][2]
        ]
        return row

    def getColumn(self, j):
        box0 = self.grid[0][j//3]
        box1 = self.grid[1][j//3]
        box2 = self.grid[2][j//3]
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
    numbers = input("Enter a list of values: ")
    board.fillBoard(numbers)
    return board

# gameBoard = createUserBoard()
#
# solve(gameBoard)
#
# gameBoard.print()
board = createUserBoard()
board.print()
