
import Image
import ImageDraw

class Engine:

    DEFAULT_COLOR = (255,0,0)  # Red

    def __init__(self):

        # All the state is maintained in a single hashmap
        # Only non-zero states are maintained (sparse representation)
        self.board = {}

        # The mapping between states and colors
        # Non-zero unmapped states are given a default color
        self.color_map = {}

    def getColor(self, state):
        if state in self.color_map:
            return self.color_map[state]
        else:
            return self.DEFAULT_COLOR

    def saveImage(self, filename, width=600, height=600):
        "Save the current state of the board into an image file"
        im = Image.new("RGB", (width, height))
        x_min, y_min, x_max, y_max = self.board.getBounds()
        x_range = x_max - x_min
        y_range = y_max - y_min
        cell_width = width / x_range
        cell_height = height / y_range
        im_draw = ImageDraw.Draw(im)
        x_pix = 0
        y_pix = 0
        for i in range(x_range):
            x_pix = i * cell_width

            for j in range(y_range):
                y_pix = j * cell_height
                im_draw.rectangle((x_pix, y_pix, x_pix+cell_width, y_pix+cell_height),
                                    fill=self.getStateColor(self.board[i][j]),
                                    outline=(100,100,100))

        im.save(filename)



    def step(self):
        "Perform one simulation step by applying each applicable rule"
        pass

    def loadRules(self, filename):
        "Load a rules file from the given filename"
        pass

    def loadConfiguration(self, filename):
        "Load a CA configuration from the given file"
        f = open(filename, 'r')
        lines = f.readlines()
        tokens = lines[0].split()
        self.width, self.height = int(tokens[0]), int(tokens[1])
        self.board = np.zeros((self.width, self.height), np.int16)

        y = 0
        for line in lines[1:]:
            line = line.strip()
            tokens = map(int, line.split())
            x = 0
            for token in tokens:
                self.board[x][y] = token
                x += 1
            y += 1


    def saveConfiguration(self, filename):
        "Save the current state of the board into a config file that can be loaded later"
        pass
