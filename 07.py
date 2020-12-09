import os
from adventofcode import AdventDay
from functools import reduce

class LuggageRuleParser:
    @staticmethod
    def parseRule(rule_string, luggage_dict) -> None:
        [color, included_bags_string] = rule_string.split(" bags contain ", 1)
        included_bags_string_lists = [ ibs.replace(" bags", "").replace(" bag", "").replace(".", "").split(" ", 1) \
                for ibs in included_bags_string.split(", ") if ibs.find("no other") == -1]
        included_bags = [(int(ibs[0]), ibs[1]) for ibs in included_bags_string_lists]
        luggage_dict[color] = included_bags
        pass
    pass
class Day07_01(AdventDay):
    def __init__(self, input_path : str) -> None:
        self.in_file = open(input_path, "r")
        self.luggage_rules = dict()
        self.contains_target = set()
        for line in self.in_file:
            LuggageRuleParser.parseRule(line.strip(), self.luggage_rules)
            pass
        pass

    def rec_rules(self, color, multiplicator=1, depth=0, target="shiny gold"):
        contain_bag_list = self.luggage_rules.get(color)
        if (color == target and not depth == 0) or color in self.contains_target:
            return True
        if (contain_bag_list is None) or len(contain_bag_list) == 0:
            return False
        for bag in contain_bag_list:
            if self.rec_rules(bag[1], multiplicator=multiplicator*bag[0], depth=depth+1):
                self.contains_target.add(color)
                return True
                pass
            pass
        return False

    def do(self) -> None:
        for lr_color in self.luggage_rules.keys():
            self.rec_rules(lr_color)
            pass
        print(len(self.contains_target))
        pass
    pass

class Day07_02(AdventDay):
    def __init__(self, input_path : str) -> None:
        self.in_file = open(input_path, "r")
        self.luggage_rules = dict()
        for line in self.in_file:
            LuggageRuleParser.parseRule(line.strip(), self.luggage_rules)
            pass
        pass

    def do(self) -> None:
        def rec_rules(color, depth = 0, count = 0):
            for bag in self.luggage_rules[color]:
                count += rec_rules(bag[1], depth=depth+1, count=0) * bag[0] + bag[0]
                pass
            return count
            pass

        print(rec_rules("shiny gold"))
        pass
    pass

input_path = os.path.dirname(os.path.realpath(__file__)) + "/07-01_input.txt"
#input_path = os.path.dirname(os.path.realpath(__file__)) + "/07-01_input_tmp.txt"
mission = Day07_01(input_path)
mission.do()
print("")
mission = Day07_02(input_path)
mission.do()