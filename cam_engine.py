
import Image
import ImageDraw
import copy
import os

from cam_board import Board
from cam_colormap import ColorMap
from cam_rules import Rules

class Engine:

    MIN_RANGE = 10

    def __init__(self):
        # All the state is maintained in a single hashmap
        # Only non-zero states are maintained (sparse representation)
        self.board = Board()

    def setColorMap(self, cm):
        "Set the Engine's ColorMap object"
        self.color_map = cm

    def setRules(self, rs):
        "Set the Engine's Rules object"
        self.rules = rs

    def saveImageRange(self, filename, x_min, y_min, x_max, y_max, width=600, height=600):
        im = Image.new("RGB", (width, height))
        x_range = x_max - x_min
        y_range = y_max - y_min
        if x_range < self.MIN_RANGE:
            x_range = self.MIN_RANGE
        if y_range < self.MIN_RANGE:
            y_range = self.MIN_RANGE
        cell_width = width / x_range
        cell_height = height / y_range
        im_draw = ImageDraw.Draw(im)
        x_pix = 0
        y_pix = 0
        for i in range(x_range):
            x_pix = i * cell_width
            for j in range(y_range):
                y_pix = j * cell_height
                state = self.board.getCell(i+x_min, j+y_min)
                im_draw.rectangle((x_pix, y_pix, x_pix+cell_width, y_pix+cell_height),
                                    fill=self.color_map.getStateColor(state),
                                    outline=(100,100,100))

        im.save(filename)

    def saveImage(self, filename, width=600, height=600, padding=3):
        "Save the current state of the board into an image file"
        x_min, y_min, x_max, y_max = self.board.getBounds()
        x_min -= padding
        x_max += padding + 1
        y_min -= padding
        y_max += padding + 1
        self.saveImageRange(filename, x_min, y_min, x_max, y_max, width, height)

    def getNeighborhood(self, center_cell):
        center_x, center_y = center_cell
        neighborhood = []
        neighborhood.append((center_x, center_y))
        neighborhood.append((center_x, center_y-1))
        neighborhood.append((center_x+1, center_y-1))
        neighborhood.append((center_x+1, center_y))
        neighborhood.append((center_x+1, center_y+1))
        neighborhood.append((center_x, center_y+1))
        neighborhood.append((center_x-1, center_y+1))
        neighborhood.append((center_x-1, center_y))
        neighborhood.append((center_x-1, center_y-1))
        return neighborhood

    def getNeighborhoodStates(self, center_cell):
        neighborhood = self.getNeighborhood(center_cell)
        neighborhood_states = []
        for n in neighborhood:
            neighborhood_states.append(self.board.getCell(n[0], n[1]))
        return neighborhood_states

    def step(self):
        "Perform one simulation step by applying each applicable rule"

        # The only cells that can change are adjacent to living cells
        new_board = copy.deepcopy(self.board)
        for live_cell in self.board.getAllCells():
            # print "Working on :", live_cell
            neighborhood = self.getNeighborhood(live_cell)
            for cell in neighborhood:
                # print "\t", cell
                # print self.getNeighborhoodStates(cell)
                match = self.rules.getRuleMatch(self.getNeighborhoodStates(cell))
                if match > -1:
                    new_board.updateCell(cell[0], cell[1], match)
        self.board = new_board


    def loadConfiguration(self, filename):
        '''Load a CA configuration from the given file.
        Should be in a sparse data format:
            x y state
        '''
        f = open(filename, 'r')
        lines = f.readlines()
        for line in lines:
            if line.strip() != '':
                x, y, state = map(int, line.split())
                self.board.updateCell(x, y, state)

    def saveConfiguration(self, filename):
        "Save the current state of the board into a config file that can be loaded later"
        out_file = open(filename, 'w')
        for x, y in self.board.getAllCells():
            out_file.write("%d %d %d\n" % (x, y, self.board.getCell(x, y)))
        out_file.close()

    def saveMovie(self, filename, steps, x1, y1, x2, y2, framerate=10):
        for i in range(steps):
            self.saveImageRange("images/image%08d.png" % (i+1), x1, y1, x2, y2)
            self.step()

        # Use FFMPEG
        command = '''ffmpeg -framerate %d -i images/image%%08d.png %s''' % (framerate, filename)
        os.system(command)


if __name__ == "__main__":
    e = Engine()
    e.loadConfiguration("test2.ca")
    rules = Rules("test2.rules")
    color_map = ColorMap("test.cm")
    e.setRules(rules)
    e.setColorMap(color_map)
    e.saveMovie("test.mov", 40, 0, 0, 100, 100, 10)
    # e.saveConfiguration("test2.ca")





