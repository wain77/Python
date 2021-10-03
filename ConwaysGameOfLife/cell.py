class Cell:
    """
    Controls the status of individual cells
    Ability to set and fetch new statuses with functions
    """

    def __init__(self):
        """ Holds the init status of the cell - dead """
        self._status = 'Dead'

    def setDead(self) -> str:
        """ Sets cell status to DEAD """
        self._status = 'Dead'

    def setAlive(self) -> str:
        """ Sets cell status to ALIVE """
        self._status = 'Alive'

    def isAlive(self) -> bool:
        """ Checks whether the cell is ALIVE or DEAD with a bool return """
        return True if self._status == 'Alive' else False

    def getPrintCharacter(self) -> str:
        """ Returns a status character to print on the board """
        return "O" if self.isAlive() else " "
