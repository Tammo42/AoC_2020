import os
from adventofcode import AdventDay

class EntryLine:
    """
    An object for one password entry
    """
    def __init__(self, min_occur, max_occur, symbol, passwd) -> None:
        self.min_occur = min_occur
        self.max_occur = max_occur
        self.symbol = symbol
        self.passwd = passwd

class Day02_01(AdventDay):
    def __init__(self, input_path) -> None:
        self.good_counter = 0
        self.bad_counter  = 0
        self.input_list = []
        for x in open(input_path):
            # get min
            parts = x.split("-", 1)
            min_occur = int(parts[0])
            x = parts[1]
            # get max
            parts = x.split(" ", 1)
            max_occur = int(parts[0])
            x = parts[1]
            # get symbol
            parts = x.split(": ", 1)
            symbol = parts[0]
            # get passwd
            passwd = parts[1].rstrip()
            entry = EntryLine(min_occur, max_occur, symbol, passwd)
            self.input_list.append(entry)
            self.results = dict()

    def check_password(self, entry) -> None:
        counter = 0
        # count the occurences of the symbol
        for sym in entry.passwd:
            if entry.symbol == sym:
                counter = counter + 1
        # check the occurences against the given constraints and create an entry
        if entry.min_occur <= counter and counter <= entry.max_occur:
            self.results[entry] = True
            self.good_counter = self.good_counter + 1
        else:
            self.results[entry] = False
            self.bad_counter = self.bad_counter + 1

    def do(self) -> None:
        for entry in self.input_list:
            self.check_password(entry)
        print("good: ", self.good_counter)
        print("bad:  ", self.bad_counter)

class Day02_02(AdventDay):
    def __init__(self, input_path) -> None:
        self.good_counter = 0
        self.bad_counter  = 0
        self.input_list = []
        for x in open(input_path):
            # get min
            parts = x.split("-", 1)
            min_occur = int(parts[0])
            x = parts[1]
            # get max
            parts = x.split(" ", 1)
            max_occur = int(parts[0])
            x = parts[1]
            # get symbol
            parts = x.split(": ", 1)
            symbol = parts[0]
            # get passwd
            passwd = parts[1].rstrip()
            entry = EntryLine(min_occur, max_occur, symbol, passwd)
            self.input_list.append(entry)
            self.results = dict()

    def check_password(self, entry) -> None:
        if entry.min_occur == 0 or entry.max_occur == 0:
            print("ERROR: Toboggan Corporate Policy does not know of this 0 you entered.")
            self.results[entry] = False
            self.bad_counter = self.bad_counter + 1
        if len(entry.passwd) < entry.max_occur:
            print("WARNING: There will not be a second letter.")
        if (entry.passwd[entry.min_occur-1] == entry.symbol) ^ (entry.passwd[entry.max_occur-1] == entry.symbol):
            self.results[entry] = True
            self.good_counter = self.good_counter + 1
        else:
            self.results[entry] = False
            self.bad_counter = self.bad_counter + 1

    def do(self) -> None:
        for entry in self.input_list:
            self.check_password(entry)
        print("good: ", self.good_counter)
        print("bad:  ", self.bad_counter)

input_path = os.path.dirname(os.path.realpath(__file__)) + "/02-01_input.txt"
mission = Day02_01(input_path)
mission.do()
print("")
mission = Day02_02(input_path)
mission.do()