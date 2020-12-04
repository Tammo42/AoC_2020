class EntryLine:
    min_occ = 0
    max_occur = 0
    symbol = ""
    passwd = ""

    def __init__(self, min_occur, max_occur, symbol, passwd):
        self.min_occur = min_occur
        self.max_occur = max_occur
        self.symbol = symbol
        self.passwd = passwd

class Day02_1:
    counter = 0
    input_list = []

    def __init__(self, input_path):
        for x in open(input_path):
            # get min
            parts = x.split("-", 1)
            min_occur = parts[0]
            x = parts[1]
            # get max
            parts = x.split(" ", 1)
            max_occur = parts[0]
            x = parts[1]
            # get symbol
            parts = x.split(": ", 1)
            symbol = parts[0]
            # get passwd
            passwd = parts[1]
            input_list.append(EntryLine(min_occur, max_occur, symbol, passwd))

    def check_password(self, min_occur, max_occur, passwd):
        pass

    def do(self):
        pass