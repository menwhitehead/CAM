

class ColorMap:

    DEFAULT_COLOR = (253,95,0)  # ORANGE

    def __init__(self, filename):
        # The mapping between states and colors
        # Non-zero unmapped states are given a default
        self.color_map = {}
        self.loadColorMap(filename)

    def addStateColor(self, state, r, g, b):
        self.color_map[state] = (r, g, b)

    def getStateColor(self, state):
        if state in self.color_map:
            return self.color_map[state]
        else:
            return self.DEFAULT_COLOR

    def loadColorMap(self, filename):
        "Load a colormap file from the given filename"
        f = open(filename, 'r')
        for line in f:
            if line.strip() != '' and line.strip()[0] != '#':
                tokens = line.split()
                state, r, g, b = map(int, tokens)  # Assign tokens to variables
                self.addStateColor(state, r, g, b)
        f.close()




