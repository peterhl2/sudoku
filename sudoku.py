from puzzles import easySudoku1, mediumSudoku1, hardSudoku1, expertSudoku1

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

    def getContainsVals(self):
        containsVals = {}
        for i in range(3):
            for j in range(3):
                if self.get(i, j):
                    containsVals.add(self.get(i, j))
        return list(containsVals)

    def getMissingVals(self):
        missingVals = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        for i in range(3):
            for j in range(3):
                val = self.get(i, j)
                if val in missingVals:
                    missingVals.remove(val)
        return list(missingVals)

    def isMissingVal(self, num):
        missingVals = self.getMissingVals()
        return num in missingVals

# 3x3 grid of Boxes for the game board
class Board:
    def __init__(self):
        self.grid = [
            [Box(), Box(), Box()],
            [Box(), Box(), Box()],
            [Box(), Box(), Box()]
        ]

    # Type input like: 1 3 4 7 9 8
    # for 81 numbers
    def fillBoard(self, numbersList):
        numbersList = numbersList.strip().split(" ")
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
        print(fullRow.format(self.getPrint(i,0), self.getPrint(i,1), self.getPrint(i,2),
                             self.getPrint(i,3), self.getPrint(i,4), self.getPrint(i,5),
                             self.getPrint(i,6), self.getPrint(i,7), self.getPrint(i,8)))
        return

    def getPrint(self, i, j):
        boardX = i // 3
        boardY = j // 3
        boxX = i % 3
        boxY = j % 3
        val = self.grid[boardX][boardY].get(boxX, boxY)
        return val if val else " "

    # TODO: Write this function, solve
    def solve(self):
        print("Given Game Board")
        self.print()
        iterations = 0
        loopUpdated = True
        while (loopUpdated):
            loopUpdated = False
            for num in range(1, 10):
                loopUpdated = self.loopFillNum(num) or loopUpdated
            iterations += 1
            print("Solve Iteration: {}".format(iterations))
            self.print()
        return

    def loopFillNum(self, num):
        updated = False
        # create matrix of empty slots which can be num
        couldBeNum = [[1]*9 for _ in range(9)]
        # clear rows/cols/box with the num
        for i in range(9):
            for j in range(9):
                cell = self.get(i, j)
                if cell > 0:
                    couldBeNum[i][j] = 0
                if cell == num:
                    for k in range(9):
                        couldBeNum[i][k] = 0
                        couldBeNum[k][j] = 0
                    top_left_idx_i = (i // 3) * 3
                    top_left_idx_j = (j % 3) * 3
                    for bi in range(3):
                        for bj in range(3):
                            couldBeNum[top_left_idx_i+bi][top_left_idx_j+bj] = 0
        # update rows
        for row in range(9):
            if self.numInRow(row, num):
                continue
            row_sum = 0
            row_idx = -1
            for col in range(9):
                if couldBeNum[row][col] and \
                   self.colIsMissingNum(col, num) and \
                   self.boxIsMissingNum(row, col, num):
                    row_sum += 1
                    row_idx = col
            if row_sum == 1:
                self.set(row, row_idx, num)
                updated = True

        # update columns
        for col in range(9):
            if self.numInCol(col, num):
                continue
            col_sum = 0
            col_idx = -1
            for row in range(9):
                if couldBeNum[row][col] and \
                   self.rowIsMissingNum(row, num) and \
                   self.boxIsMissingNum(row, col, num):
                    col_sum += 1
                    col_idx = row
            if col_sum == 1:
                self.set(col_idx, col, num)
                updated = True

        # update boxes
        for box in range(9):
            box_sum = 0
            box_idx = -1
            top_left_idx_i = (box // 3) * 3
            top_left_idx_j = (box % 3) * 3
            for i in range(3):
                for j in range(3):
                    if couldBeNum[top_left_idx_i+i][top_left_idx_j+j] and \
                       self.rowIsMissingNum(top_left_idx_i+i, num) and \
                       self.colIsMissingNum(top_left_idx_j, num):
                        box_sum += 1
                        box_idx = (top_left_idx_i+i, top_left_idx_j+j)
            if box_sum == 1:
                self.set(box_idx[0], box_idx[1], num)
                updated = True

        return updated

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
        row = []
        for col in range(9):
            row.append(self.get(i, col))
        return row

    def getCol(self, j):
        col = []
        for row in range(9):
            col.append(self.get(row, j))
        return col

    def getBox(self, i, j):
        return self.grid[i // 3][j // 3]

    def getAllBoxes(self):
        boxes = []
        for i in range(9):
            boxes.append(self.getBox(i // 3, i % 3))
        return boxes

    def numInRow(self, i, num):
        return num in self.getRow(i)

    def numInCol(self, j, num):
        return num in self.getCol(j)

    def numInBox(self, i, j, num):
        self.getBox(i, j)

    def getMissingValsRow(self, i):
        missingVals = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        for j in range(9):
            val = self.get(i, j)
            if val in missingVals:
                missingVals.remove(val)
        return list(missingVals)

    def getMissingValsCol(self, j):
        missingVals = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        for i in range(9):
            val = self.get(i, j)
            if val in missingVals:
                missingVals.remove(val)
        return list(missingVals)

    def rowIsMissingNum(self, i, num):
        return num in self.getMissingValsRow(i)

    def colIsMissingNum(self, j, num):
        return num in self.getMissingValsCol(j)

    def boxIsMissingNum(self, i, j, num):
        return num in self.getBox(i, j).getMissingVals()

def createBlankBoard():
    return Board()

def createUserBoard():
    board = Board()
    numbers = input("Enter a list of values: ")
    board.fillBoard(numbers)
    return board

def loadUserBoard(input):
    board = Board()
    board.fillBoard(input)
    return board

board = loadUserBoard(expertSudoku1)
board.solve()
