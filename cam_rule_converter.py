
import itertools
import copy

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

    def generateWildcardRules(self, neighborhood, new_state, starting=0):
        #r = Rule([old]+list(lst), new)
        rules = []
        found_wildcard = False
        index = 0
        for token in neighborhood[starting:]:
            if token[0] == '[':   # a range of possible states
                found_wildcard = True
                start_range, end_range = map(int, token[1:-1].split('-'))
                # print token[1:-1]
                # print start_range, end_range
                for i in range(start_range, end_range+1):
                    new_neighborhood = copy.deepcopy(neighborhood)
                    new_neighborhood[index] = i
                    result = self.generateWildcardRules(new_neighborhood, new_state, starting=index+1)
                    # print type(result)
                    rules.append(result)
            index += 1
        if not found_wildcard:
            return Rule(neighborhood, new_state)
        else:
            return rules


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
                elif line[0].lower() == '*':
                    # print "WILDCARD RULE"
                    tokens = line[1:].split()
                    #tokens = map(int, line[1:].split())
                    # print old_state, neighbor_count, new_state
                    x = self.generateWildcardRules(tokens[:-1], tokens[-1])
                    for element in x:
                        print element
                    #r = Rule(tokens[0:-1], tokens[-1])
                    #self.addRule(r)
        f.close()


if __name__=="__main__":
    rc = RuleConverter()
    rc.loadRules("high.rules")


