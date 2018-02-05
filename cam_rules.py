

class Rule:

    def __init__(self, n, ne, e, se, s, sw, w, nw, new):
        self.n = n
        self.ne = ne
        self.e = e
        self.se = se
        self.s = s
        self.sw = sw
        self.w = w
        self.nw = nw
        self.c = c
        self.new = new


class Rules:

    def __init__(self):
        # Transition rules
        self.rules = []

    def addRule(self, rule):
        self.rules.append(rule)

    def loadRules(self, filename):
        "Load a rules file from the given filename"
        f = open(filename, 'r')
        for line in f:
            tokens = line.split()
            c, n, ne, e, se, s, sw, w, nw, new = tokens  # Assign tokens to variables
            r = Rule(c, n, ne, e, se, s, sw, w, nw, new)
            self.addRule(r)
        f.close()




