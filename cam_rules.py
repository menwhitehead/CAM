

class Rule:

    def __init__(self, neighborhood, new):
        self.neighborhood = neighborhood
        self.new = new

    def __eq__(self, other):
        for i in range(len(self.neighborhood)):
            if self.neighborhood[i] != -1 and self.neighborhood[i] != other.neighborhood[i]:
                return False
        return True


class Rules:

    def __init__(self, filename):
        # Transition rules
        self.rules = []
        self.loadRules(filename)

    def addRule(self, rule):
        self.rules.append(rule)

    def getRuleMatch(self, neighborhood):
        possible_rule = Rule(neighborhood, None)
        for rule in self.rules:
            if rule == possible_rule:
                return rule.new
        return -1

    def loadRules(self, filename):
        "Load a rules file from the given filename"
        f = open(filename, 'r')
        for line in f:
            if line.strip() != '' and line.strip()[0] != '#':
                tokens = map(int, line.split())
                # old, n, ne, e, se, s, sw, w, nw, new = tokens  # Assign tokens to variables
                r = Rule(tokens[0:-1], tokens[-1])
                self.addRule(r)
        f.close()




