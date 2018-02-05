

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
        xs = self.by_x.keys()
        x_min, x_max = min(xs), max(xs)

        ys = self.by_y.keys()
        y_min, y_max = min(ys), max(ys)

        return (x_min, y_min, x_max, y_max)

    def updateCell(self, x, y, state):
        "Update the (x,y) cell to have state"
        if x not in self.by_x:
            self.by_x[x] = {}
        self.by_x[x][y] = state

        if y not in self.by_y:
            self.by_y[y] = {}
        self.by_y[y][x] = state

        self.by_full_key[(x,y)] = state

    def removeCell(self, x, y):
        "Kill off the cell at (x,y)"
        if x in self.by_x and y in self.by_x[x]:
            del self.by_x[x][y]
        if y in self.by_y and x in self.by_y[y]:
            del self.by_y[y][x]
        del self.by_full_key[(x,y)]

    def getCell(self, x, y):
        if (x, y) in self.by_full_key:
            return self.by_full_key[(x, y)]
        else:
            return 0 # dead cell

    def getAllCells(self):
        return self.by_full_key.keys()

    def __str__(self):
        result = ""
        result += str(self.by_x) + "\n"
        result += str(self.by_y) + "\n"
        result += str(self.by_full_key)
        return result



