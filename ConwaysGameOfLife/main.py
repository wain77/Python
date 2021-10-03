"""
Conway's Game of Life
Sam Wainwright
From a tutorial by Martin A. Aaberge
https://medium.com/better-programming/how-to-write-conwells-game-of-life-in-python-c6eca19c4676
"""

from board import Board


def main():
    userRows = int(input('how many rows? '))
    userColumns = int(input('how many columns? '))

    gameOfLifeBoard = Board(userRows, userColumns)

    gameOfLifeBoard.drawBoard()

    userAction = ''
    while userAction != 'q':
        userAction = input('Press enter to add a generation or q to quit: ')

        if userAction == '':
            gameOfLifeBoard.updateBoard()
            gameOfLifeBoard.drawBoard()


main()
