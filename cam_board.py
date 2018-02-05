

class Board:

    # All non-zero states organized by x position first
    by_x = {}

    # All non-zero states organized by y position first
    by_y = {}

    # All non-zero states organized together by x,y
    by_full_key = {}


    def __init__(self):
        pass


    def updateCell(self, x, y, state):
        "Update the (x,y) cell to have state"
        pass

    def removeCell(self, x, y):
        "Kill off the cell at (x,y)"
        pass

    def getCell(self, x, y):
        return self.by_full_key((x, y))



