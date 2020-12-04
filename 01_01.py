# create a dictionary for the results
# start a thread for each index (alternatively go through the array with a map and a threadpool)
# calculate the sum for all following elements and return the element if it creates the correct result, otherwise return null
# evaluate the results array


# optimization 1:
# sort the array first and only calculate results while the number is low enough
# optimization 2:
# only start a thread if the number is low enough in the first place

import os

class Day01_01:
    results = dict()
    number_list = []

    def __init__(self, input_path):
        for line in open(input_path, "r"):
            self.number_list.append(int(line))
        # parse the input file
        self.number_list = self.number_list.sort()

    def do(self, target_sum):
        for index, number in enumerate(self.number_list):
            self.test_number(target_sum, index)
            if number in results:
                print(number, " + ", results[number], " = ", 2020, "\n")
                print(number, " * ", results[number], " = ", number * results[number] , "\n")
                break

    def test_number(self, result, index):
        a = self.number_list[index]
        for b in self.number_list.reverse():
            r = a + b
            if r == result:
                self.results.update({a: b})
                break
            elif r < result:
                break

print(os.path.dirname(os.path.realpath(__file__))
#Day01_01() + "").do(2020)