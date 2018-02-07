
import itertools

from cam_rules import *

class RuleConverter:
    "Convert high-level rules into base rules"

    def __init__(self):
        # Transition rules
        self.rules = []

    def generateNeighborCountRule(self, old, neighbor_count, new):
        '''Generate basic rules for the high-level rule for neighbor counts'''
        #neighborhood = [old, 0, 0, 0, 0, 0, 0, 0, 0]
        all_binary = list(itertools.product([0, 1], repeat=8))
        right_number = list(filter(lambda x: sum(x) == neighbor_count, all_binary))
        # print right_number
        for lst in right_number:
            r = Rule([old]+list(lst), new)
            print r

        # print lst

        # r = Rule(neighborhood, new)
        # print r

    def loadRules(self, filename):
        "Load a high-level rules file from the given filename"
        f = open(filename, 'r')
        for line in f:
            line = line.strip()
            if line != '' and line[0] != '#':
                # A neighborhood count rule
                if line[0].lower() == 'n':
                    # print "NEIGHBORHOOD COUNT RULE"
                    old_state, neighbor_count, new_state = map(int, line[1:].split())
                    # print old_state, neighbor_count, new_state
                    self.generateNeighborCountRule(old_state, neighbor_count, new_state)
                    #r = Rule(tokens[0:-1], tokens[-1])
                    #self.addRule(r)
        f.close()


if __name__=="__main__":
    rc = RuleConverter()
    rc.loadRules("high.rules")


