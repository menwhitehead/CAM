

class Rule:

    def __init__(self, neighborhood, new):
        neighborhood = map(int, neighborhood)  # ensure integers
        self.neighborhood = neighborhood
        self.new = new

    def __eq__(self, other):
        for i in range(len(self.neighborhood)):
            if self.neighborhood[i] != -1 and self.neighborhood[i] != other.neighborhood[i]:
                return False
        return True

    def __str__(self):
        return str(self.neighborhood[0]) + " " + str(self.neighborhood[1:])[1:-1].replace(',', '') + " " + str(self.new)


class Rules:

    def __init__(self, filename):
        # Transition rules
        self.rules = {}
        self.loadRules(filename)

    def addRule(self, rule_pattern, new_state):
        self.rules[rule_pattern] = new_state

    def getRuleMatch(self, neighborhood):
        neighborhood_tuple = tuple(neighborhood)
        #possible_rule = Rule(neighborhood, None)
        if neighborhood_tuple in self.rules:
            return self.rules[neighborhood_tuple]
        return -1

    def loadRules(self, filename):
        "Load a rules file from the given filename"
        f = open(filename, 'r')
        for line in f:
            if line.strip() != '' and line.strip()[0] != '#':
                tokens = map(int, line.split())
                # old, n, ne, e, se, s, sw, w, nw, new = tokens  # Assign tokens to variables
                #r = Rule(tokens[0:-1], tokens[-1])
                self.addRule(tuple(tokens[0:-1]), tokens[-1])
        f.close()




