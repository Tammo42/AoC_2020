# TODO start a thread for each index (alternatively go through the array with a map and a threadpool)

import os

class Day01_01:
    def __init__(self, input_path):
        # initialize the first puzzle
        # create a results dict, parse the list of numbers and sort it
        self.results = dict()
        self.number_list = list()
        for line in open(input_path, "r"):
            self.number_list.append(int(line))
        self.number_list.sort()
        # create a reversed version for easy access and optimization
        self.reverse_number_list = self.number_list.copy()
        self.reverse_number_list.reverse()
        return

    def do(self, target_sum):
        # evaluate the number list items
        if self.number_list is not None:
            for index, number in enumerate(self.number_list):
                self.test_number(target_sum, index)
                # check the results
                if number in self.results:
                    print(number, " + ", self.results[number], " = ", 2020)
                    print(number, " * ", self.results[number], " = ", number * self.results[number])
                    break
        else:
            print("The number list was None!")
        print(self.results.values())

    def test_number(self, result, index):
        # check if the number at the index and a number from the list form the result sum
        a = self.number_list[index]
        # go backwards through the sortet list and stop when the sums get too low
        for b in self.reverse_number_list:
            r = a + b
            if r == result:
                # found the needed entry
                self.results.update({a: b})
                break
            elif r < result:
                # the sum can no longer be reached, no need to check further
                break

class Day01_02:
    def __init__(self, input_path):
        # initialize the first puzzle
        # create a results dict, parse the list of numbers and sort it
        self.results = dict()
        self.number_list = list()
        for line in open(input_path, "r"):
            self.number_list.append(int(line))
        self.number_list.sort()
        # create a reversed version for easy access and optimization
        self.reverse_number_list = self.number_list.copy()
        self.reverse_number_list.reverse()
        return

    def do(self, target_sum):
        # evaluate the number list items
        if self.number_list is not None:
            for index, number in enumerate(self.number_list):
                self.test_number(target_sum, index)
                # check the results
                if number in self.results:
                    print( number
                         , " + ", self.results[number][0]
                         , " + ", self.results[number][1]
                         , " = ", 2020
                         )
                    print( number
                         , " * ", self.results[number][0]
                         , " * ", self.results[number][1]
                         , " = ", number * self.results[number][0] * self.results[number][1]
                         )
                    break
        else:
            print("The number list was None!")
        print(self.results.values())

    def test_number(self, result, index):
        a = self.number_list[index]
        for b in self.reverse_number_list:
            if a+b > result:
                continue
            for c in self.number_list:
                r = a + b + c
                if r == result:
                    # found the needed entry
                    self.results.update({a: (b,c)})
                    return
                elif r > result:
                    # the sum can no longer be reached, no need to check further
                    break

input_path = os.path.dirname(os.path.realpath(__file__)) + "/01-01_input.txt"
mission = Day01_01(input_path)
mission.do(2020)
print("")
mission = Day01_02(input_path)
mission.do(2020)