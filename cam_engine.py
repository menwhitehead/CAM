
import Image
import ImageDraw

class Engine:

    DEFAULT_COLOR = (255,0,0)  # Red

    # All the state is maintained in a single hashmap
    # Only non-zero states are maintained (sparse representation)
    board = {}

    # The mapping between states and colors
    # Non-zero unmapped states are given a default color
    color_map = {}

    def __init__(self):
        pass

    def getColor(self, state):
        if state in self.color_map:
            return self.color_map[state]
        else:
            return self.DEFAULT_COLOR

    def getBounds(self):
        "Return the coordinates for the bounding box of the non-zero cells"
        pass

    def saveImage(self, filename, width=600, height=600):
        "Save the current state of the board into an image file"
        im = Image.new("RGB", (self.width * cell_size+1, self.height * cell_size+1))
        im_draw = ImageDraw.Draw(im)
        x_pix = 0
        y_pix = 0
        for i in range(self.width):
            x_pix = i * cell_size

            for j in range(self.height):
                y_pix = j * cell_size
                im_draw.rectangle((x_pix, y_pix, x_pix+cell_size, y_pix+cell_size),
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
