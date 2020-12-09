import os
from adventofcode import AdventDay

class Day08_01(AdventDay):
    def __init__(self, input_path : str) -> None:
        self.in_file = open(input_path, "r")
        pass

    def do(self) -> None:
        pass
    pass

class Day08_02(AdventDay):
    def __init__(self, input_path : str) -> None:
        self.in_file = open(input_path, "r")
        pass

    def do(self) -> None:
        pass
    pass

input_path = os.path.dirname(os.path.realpath(__file__)) + "/07-01_input.txt"
mission = Day07_01(input_path)
mission.do()
print("")
mission = Day07_02(input_path)
mission.do()