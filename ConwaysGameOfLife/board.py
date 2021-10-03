from cell import Cell
from random import randint


class Board:
    """
    Generate, and draw the board
    Check cell neighbours and update status for next tick
    """

    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self._grid = [[Cell() for columnCells in range(self._columns)]
                      for rowCells in range(self._rows)]

        self._generateBoard()

    def drawBoard(self):
        print('\n' * 40)
        print('printing board')
        for row in self._grid:
            for column in row:
                print(column.getPrintCharacter(), end='')
            print()

    def _generateBoard(self):
        for row in self._grid:
            for column in row:
                if randint(0, 2) == 1:
                    column.setAlive()

    def checkNeighbour(self, checkRow, checkColumn):
        # How deep is the search?
        searchMin = -1
        searchMax = 2

        # Empty list for neighbour cell info
        neighbourList = []
        for row in range(searchMin, searchMax):
            for column in range(searchMin, searchMax):
                neighbourRow = checkRow + row
                neighbourColumn = checkColumn + column

                validNeighbour = True

                if neighbourRow == checkRow and neighbourColumn == checkColumn:
                    validNeighbour = False

                if neighbourRow < 0 or neighbourRow >= self._rows:
                    validNeighbour = False

                if neighbourColumn < 0 or neighbourColumn >= self._columns:
                    validNeighbour = False

                if validNeighbour:
                    neighbourList.append(
                        self._grid[neighbourRow][neighbourColumn])

        return neighbourList

    def updateBoard(self):
        print('updating board')

        # Lists for holding next tick cell status
        goAlive = []
        goDead = []

        for row in range(len(self._grid)):
            for column in range(len(self._grid[row])):
                # Check neighbour for each square
                checkNeighbour = self.checkNeighbour(row, column)

                liveNeighboursCount = []
                for neighbourCell in checkNeighbour:
                    if neighbourCell.isAlive():
                        liveNeighboursCount.append(neighbourCell)

                cellObject = self._grid[row][column]
                statusMainCell = cellObject.isAlive()

                if statusMainCell:
                    if len(liveNeighboursCount) < 2 or len(liveNeighboursCount) > 3:
                        goDead.append(cellObject)

                        if len(liveNeighboursCount) == 3 or len(liveNeighboursCount) == 2:
                            goAlive.append(cellObject)

                else:
                    if len(liveNeighboursCount) == 3:
                        goAlive.append(cellObject)

        for cellItem in goAlive:
            cellItem.setAlive()

        for cellItem in goDead:
            cellItem.setDead()
