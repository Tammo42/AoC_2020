from adventofcode import AdventDay
import os

class Day10_01(AdventDay):
    def __init__(self, input_path : str) -> None:
        self.in_numbers = list()
        for line in open(input_path, "r"):
            line = line.strip()
            self.in_numbers.append(int(line))
            pass
        self.sorted_in_numbers = self.in_numbers.copy()
        self.sorted_in_numbers.sort()
        pass

    def do(self) -> None:
        diff1 = 0
        diff2 = 0
        diff3 = 0
        for i, x in enumerate(self.sorted_in_numbers):
            if i == 0:
                if x == 1:
                    diff1 +=1
                elif x == 2:
                    diff2 +=1
                elif x == 3:
                    diff3 +=1
                else:
                    raise Exception("The difference is too big!")
                pass
            j = i + 1
            if j == len(self.sorted_in_numbers):
                diff3 += 1
                pass
            else:
                y = self.sorted_in_numbers[j]
                d = y-x
                if d == 1:
                    diff1 +=1
                elif d == 2:
                    diff2 +=1
                elif d == 3:
                    diff3 +=1
                else:
                    raise Exception("The difference is too big!")
                pass
            pass
        print(diff1, diff2, diff3)
        print("The product is", diff1*diff3)
        pass
    pass

class Day10_02(AdventDay):
    def __init__(self, input_path : str) -> None:
        self.calculated = dict()
        self.in_numbers = list()
        for line in open(input_path, "r"):
            line = line.strip()
            self.in_numbers.append(int(line))
            pass
        self.sorted_in_numbers = self.in_numbers.copy()
        self.sorted_in_numbers.append(0)
        self.sorted_in_numbers.sort()
        pass

    def rec_chain(self, index=0) -> int:
        next_numbers = [x for x \
                in self.sorted_in_numbers[index+1:min(index+4,len(self.sorted_in_numbers))] \
                if x < self.sorted_in_numbers[index]+4]
        if not next_numbers:
            if index == len(self.sorted_in_numbers)-1:
                return 1
            else:
                raise Exception("Next_numbers was empty at index", index)
            pass
        sum = 0
        for i in range(len(next_numbers)):
            current_index = index + 1 + i
            sum += self.calculated[current_index] if current_index in self.calculated else self.rec_chain(index=current_index)
            pass
        self.calculated[index] = sum
        return sum

    def do(self) -> None:
        print(self.rec_chain())
        pass
    pass

input_path = os.path.dirname(os.path.realpath(__file__)) + "/10-01_input.txt"
mission = Day10_01(input_path)
mission.do()
print("")
mission = Day10_02(input_path)
mission.do()