

class Board:

    def __init__(self):
        # All non-zero states organized by x position first
        self.by_x = {}

        # All non-zero states organized by y position first
        self.by_y = {}

        # All non-zero states organized together by x,y
        self.by_full_key = {}


    def getBounds(self):
        "Return the coordinates for the bounding box of the non-zero cells"
        pass

    def updateCell(self, x, y, state):
        "Update the (x,y) cell to have state"
        pass

    def removeCell(self, x, y):
        "Kill off the cell at (x,y)"
        pass

    def getCell(self, x, y):
        return self.by_full_key((x, y))



