
import Image
import ImageDraw

from cam_board import Board

class Engine:

    DEFAULT_COLOR = (253,95,0)  # ORANGE
    MIN_RANGE = 10

    def __init__(self):

        # All the state is maintained in a single hashmap
        # Only non-zero states are maintained (sparse representation)
        self.board = Board()

        # The mapping between states and colors
        # Non-zero unmapped states are given a default color
        self.color_map = {
            0:(0,0,0),
            1:(0,255,0),
            2:(0,0,255)
            }

    def getStateColor(self, state):
        if state in self.color_map:
            return self.color_map[state]
        else:
            return self.DEFAULT_COLOR

    def saveImage(self, filename, width=600, height=600, padding=3):
        "Save the current state of the board into an image file"
        im = Image.new("RGB", (width, height))
        x_min, y_min, x_max, y_max = self.board.getBounds()
        x_min -= padding
        x_max += padding + 1
        y_min -= padding
        y_max += padding + 1

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
                                    fill=self.getStateColor(state),
                                    outline=(100,100,100))

        im.save(filename)



    def step(self):
        "Perform one simulation step by applying each applicable rule"
        pass

    def loadRules(self, filename):
        "Load a rules file from the given filename"
        pass

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


if __name__ == "__main__":
    e = Engine()
    e.loadConfiguration("test.ca")
    e.saveImage("test.png")
    e.saveConfiguration("test2.ca")