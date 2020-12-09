import os
from adventofcode import AdventDay

PLANE_ROWS = int(128)
PLANE_COLUMS = int(8)
RC_SEPARATOR = int(7)

class Plane:
    def __init__(self) -> None:
        self.__rows = list()
        for r in range(PLANE_ROWS):
            seats = list()
            for c in range(PLANE_COLUMS):
                seats.append((r*8+c, True))
                pass
            self.__rows.append(seats)
            pass
        pass

    def reserve_seat(self, row : int, column : int, seat_id) -> None:
        self.__rows[row][column] = (seat_id, False)
        pass

    def get_free_seats(self) -> list:
        free_seats = list()
        for r in self.__rows:
            for s in r:
                if s[1]:
                    free_seats.append(s[0])
                    pass
                pass
            pass
        return free_seats
    pass

class BoardingPass:
    @staticmethod
    def __get_seat_row(seat_number : str) -> int:
        row_number = seat_number[:RC_SEPARATOR]
        rows = list()
        for i in range(PLANE_ROWS):
            rows.append(int(i))
            pass
        for symbol in row_number:
            if symbol == "F":
                rows = rows[:len(rows)//2]
                pass
            elif symbol == "B":
                rows = rows[len(rows)//2:]
                pass
            else:
                print("ERROR unexpected row identifier:", symbol)
                pass
            pass
        return rows[0]

    @staticmethod
    def __get_seat_column(seat_number : str) -> int:
        col_number = seat_number[RC_SEPARATOR:]
        cols = list()
        for i in range(PLANE_COLUMS):
            cols.append(int(i))
            pass
        for symbol in col_number:
            if symbol == "L":
                cols = cols[:len(cols)//2]
                pass
            elif symbol == "R":
                cols = cols[len(cols)//2:]
                pass
            else:
                print("ERROR unexpected column identifier:", symbol)
                pass
            pass
        return cols[0]

    @staticmethod
    def __get_seat_id(seat_number : str) -> int:
        return BoardingPass.__get_seat_row(seat_number) * 8 \
            + BoardingPass.__get_seat_column(seat_number)
    
    def __init__(self, plane : Plane, seat_number : str) -> None:
        self.__seat_number = seat_number
        self.__plane = plane
        self.__row = BoardingPass.__get_seat_row(seat_number)
        self.__column = BoardingPass.__get_seat_column(seat_number)
        self.__seat_id = BoardingPass.__get_seat_id(seat_number)
        self.reserve()
        pass

    def get_seat_number(self) -> str:
        return self.__seat_number

    def get_seat_row(self) -> int:
        return self.__row

    def get_seat_column(self) -> int:
        return self.__column
    
    def get_seat_id(self) -> int:
        return self.__seat_id

    def reserve(self) -> None:
        self.__plane.reserve_seat(self.get_seat_row(), self.get_seat_column(), self.get_seat_id())
        pass

class Day05_01(AdventDay):
    def __init__(self, input_path : str) -> None:
        self.__plane = Plane()
        self.__boarding_pass_numbers = list()
        for line in open(input_path, "r"):
            line = line.strip()
            self.__boarding_pass_numbers.append(line)
            pass

    def do(self) -> None:
        highest_id = 0
        for bpn in self.__boarding_pass_numbers:
            bp = BoardingPass(self.__plane, bpn)
            sid = bp.get_seat_id()
            if highest_id < sid:
                highest_id = sid
                pass
            pass
        print("The highest seat id is", highest_id)
        pass
    pass

class Day05_02(AdventDay):
    def __init__(self, input_path : str) -> None:
        self.__plane = Plane()
        self.__boarding_pass_numbers = list()
        self.__boarding_passes = list()
        for line in open(input_path, "r"):
            line = line.strip()
            self.__boarding_pass_numbers.append(line)
            pass

    def do(self) -> None:
        for bpn in self.__boarding_pass_numbers:
            self.__boarding_passes.append(BoardingPass(self.__plane, bpn))
            pass
        free_seats = self.__plane.get_free_seats()
        valid_free_seats = list()
        for i in range(1, len(free_seats)):
            if free_seats[i]-1 not in free_seats \
                and free_seats[i]+1 not in free_seats:
                valid_free_seats.append(free_seats[i])
                pass
            pass
        print("The empty seat is:", valid_free_seats[0])
        pass
    pass

input_path = os.path.dirname(os.path.realpath(__file__)) + "/05-01_input.txt"
mission = Day05_01(input_path)
mission.do()
print("")
mission = Day05_02(input_path)
mission.do()
