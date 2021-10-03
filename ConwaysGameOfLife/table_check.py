class TableCheck(object):
    """ Tablecheck test class """

    def __init__(self):
        self._grid = [['A', 'B', 'C'],
                      ['D', 'E', 'F'],
                      ['G', 'H', 'I']]

    def printGrid(self):
        for row in self._grid:
            print(row)
