from adventofcode import AdventDay
from concurrent.futures import ThreadPoolExecutor
import os

def prev_n(li, index, count=0) -> list:
    if index < count:
        raise Exception("prevn: " + "The index was too low to provide " + str(count) + " numbers.")
    return li[max(index-count,0):index]

def build_combination_list(li, index, count=0) -> set:
    sums = set()
    if index < count:
        raise Exception("build_combination_list: " + "The index was too low to provide " + str(count) + " numbers.")
    prev = prev_n(li, index, count=count)
    for i, x in enumerate(prev[:-1]):
        for y in prev[i+1:]:
            sums.add(x+y)
            pass
        pass
    return sums

def find_number_without_prev_pair(li, count=0) -> int:
    if len(li) <= count:
        raise Exception("find_number_without_prev_pair: " + "The provided list is not long enough for a count of " + str(count))
    for i, n in enumerate(li):
        if i < count:
            continue
        try:
            if n not in build_combination_list(li, i, count=count):
                print(n, "is not a sum of a pair of previous numbers.")
                return n
            pass
        except Exception as exc:
            print("find_number_without_prev_pair:", "An error occured.", str(exc))
            pass
        pass
    pass

def find_contigous_sum_range(li, target) -> (int, int):
    for i, x in enumerate(li[:-1]):
        sum = x
        for j, y in enumerate(li[i+1:]):
            sum += y
            if sum == target:
                return (i,i+1+j)
            elif sum > target:
                break
            pass
        pass
    pass

class Day09_01(AdventDay):
    def __init__(self, input_path : str) -> None:
        self.in_numbers = list()
        for line in open(input_path, "r"):
            line = line.strip()
            self.in_numbers.append(int(line))
            pass
        pass

    def do(self) -> None:
        count = 25
        find_number_without_prev_pair(self.in_numbers, count=count)
        pass
    pass

class Day09_02(AdventDay):
    def __init__(self, input_path : str) -> None:
        self.in_numbers = list()
        for line in open(input_path, "r"):
            line = line.strip()
            self.in_numbers.append(int(line))
            pass
        pass

    def do(self) -> None:
        count = 25
        n = find_number_without_prev_pair(self.in_numbers, count=count)
        (min, max) = find_contigous_sum_range(self.in_numbers, n)
        print("The numbers from the lines", min, "to", max, "sum up to", n, ".")
        #print("The sum of the numbers", self.in_numbers[min], "(at", min, ") and" \
                #, self.in_numbers[max], "(at ", max, ") is", self.in_numbers[min]+self.in_numbers[max])

        smallest = self.in_numbers[min]
        largest  = 0
        for x in self.in_numbers[min:max]:
            if x < smallest:
                smallest = x
                pass
            if largest  < x:
                largest = x
                pass
            pass

        print("The sum of the smallest (" + str(smallest) + ") and largest" \
                + " number (" + str(largest) + ") is", smallest+largest)
        pass
    pass

input_path = os.path.dirname(os.path.realpath(__file__)) + "/09-01_input.txt"
mission = Day09_01(input_path)
mission.do()
print("")
mission = Day09_02(input_path)
mission.do()