import os
from adventofcode import AdventDay
from functools import reduce

class Day06_01(AdventDay):
    def __init__(self, input_path : str) -> None:
        # [[str]] <= a list of flight groups with a list of the answers string of each person
        in_file = open(input_path, "r")
        self.input = [[flight_passenger for flight_passenger in flight_group.split("\n") if (flight_passenger != "")] \
                for flight_group in in_file.read().split("\n\n")]
        pass

    def do(self) -> None:
        group_answers = []
        for group in self.input:
            answers = ""
            for person in group:
                for answer in person:
                    if answer not in answers:
                        answers += answer
                        pass
                    pass
                pass
            group_answers.append(answers)
            pass
        print(len(reduce(lambda res, item: res + item, group_answers, "")))
        pass
    pass

class Day06_02(AdventDay):
    def __init__(self, input_path : str) -> None:
        # [[str]] <= a list of flight groups with a list of the answers string of each person
        in_file = open(input_path, "r")
        self.input = [[flight_passenger for flight_passenger in flight_group.split("\n") if (flight_passenger != "")] \
                for flight_group in in_file.read().split("\n\n")]
        pass

    def do(self) -> None:
        group_answers = []
        for group in self.input:
            answers = group[0]
            first = True
            for person in group:
                if first:
                    first = False
                    pass
                else:
                    for answer in answers:
                        if answer not in person:
                            answers = answers.replace(answer, "")
                            pass
                        pass
                    pass
                pass
            group_answers.append(answers)
            pass
        print(len(reduce(lambda res, item: res + item, group_answers, "")))
        pass
    pass

input_path = os.path.dirname(os.path.realpath(__file__)) + "/06-01_input.txt"
mission = Day06_01(input_path)
mission.do()
print("")
mission = Day06_02(input_path)
mission.do()