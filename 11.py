from adventofcode import AdventDay
from enum import Enum
import os

class FieldType(Enum):
    TAKEN = 0
    EMPTY = 1
    FLOOR = 2
    pass

class ConwaysGrid:
    def __init__(self, start : str):
        ys = start.split("\n")
        self.seats = dict()
        self.ydim = len(ys)
        for j, y in enumerate(ys):
            self.xdim = len(y)
            for i, x in enumerate(y):
                coords = (i, j)
                if x == "L":
                    self.seats[coords] = FieldType.EMPTY
                    pass
                pass
            pass
        #self.print()
        pass

    def print(self):
        for j in range(self.ydim):
            for  i in range(self.xdim):
                ft = self.seats.get((i, j), FieldType.FLOOR)
                if ft == FieldType.FLOOR:
                    print(".", end="")
                    pass
                elif ft == FieldType.TAKEN:
                    print("#", end="")
                    pass
                else:
                    print("L", end="")
                    pass
                pass
            print()
            pass
        print()
        pass

    def count_filled(self) -> int:
        counter = 0
        for s in self.seats.values():
            if s == FieldType.TAKEN:
                counter += 1
            pass
        return counter

    def count_filled_seen(self,coords) -> int:
        dirs = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
        filled = 0
        for xdir,ydir in dirs:
            in_bounds = lambda x, y: 0 <= x and x < self.xdim and 0 <= y and y < self.ydim
            x, y = (coords[0]+xdir, coords[1]+ydir)
            while in_bounds(x, y) and self.seats.get((x,y), FieldType.FLOOR) == FieldType.FLOOR:
                #print((x,y), self.seats.get((x,y), FieldType.FLOOR))
                x += xdir
                y += ydir
                #print((x,y), self.seats.get((x,y), FieldType.FLOOR))
                #print()
                pass
            else:
                if self.seats.get((x,y), FieldType.EMPTY) == FieldType.TAKEN:
                    filled += 1
                    pass
                pass
            pass
        #print(coords,filled)
        return filled

    def count_filled_neighbors(self, coords) -> int:
        taken_neighbour_seats = 0

        ul = (coords[0]-1, coords[1]-1)
        if self.seats.get(ul, FieldType.FLOOR) == FieldType.TAKEN:
            taken_neighbour_seats += 1
            pass
        um = (coords[0]-1, coords[1])
        if self.seats.get(um, FieldType.FLOOR) == FieldType.TAKEN:
            taken_neighbour_seats += 1
            pass
        ur = (coords[0]-1, coords[1]+1)
        if self.seats.get(ur, FieldType.FLOOR) == FieldType.TAKEN:
            taken_neighbour_seats += 1
            pass
        ml = (coords[0], coords[1]-1)
        if self.seats.get(ml, FieldType.FLOOR) == FieldType.TAKEN:
            taken_neighbour_seats += 1
            pass
        mr = (coords[0], coords[1]+1)
        if self.seats.get(mr, FieldType.FLOOR) == FieldType.TAKEN:
            taken_neighbour_seats += 1
            pass
        ll = (coords[0]+1, coords[1]-1)
        if self.seats.get(ll, FieldType.FLOOR) == FieldType.TAKEN:
            taken_neighbour_seats += 1
            pass
        lm = (coords[0]+1, coords[1])
        if self.seats.get(lm, FieldType.FLOOR) == FieldType.TAKEN:
            taken_neighbour_seats += 1
            pass
        lr = (coords[0]+1, coords[1]+1)
        if self.seats.get(lr, FieldType.FLOOR) == FieldType.TAKEN:
            taken_neighbour_seats += 1
            pass

        return taken_neighbour_seats

    def check_seat(self, coords) -> FieldType:
        field_type = self.seats[coords]
        if field_type == FieldType.TAKEN:
            if 3 < self.count_filled_neighbors(coords=coords):
                return FieldType.EMPTY
            else:
                return FieldType.TAKEN
            pass
        elif field_type == FieldType.EMPTY:
            if self.count_filled_neighbors(coords=coords) < 1:
                return FieldType.TAKEN
            else:
                return FieldType.EMPTY
            pass
        else:
            return FieldType.FLOOR
        pass

    def check_seat2(self, coords) -> FieldType:
        field_type = self.seats[coords]
        if field_type == FieldType.TAKEN:
            if 4 < self.count_filled_seen(coords=coords):
                return FieldType.EMPTY
            else:
                return FieldType.TAKEN
            pass
        elif field_type == FieldType.EMPTY:
            if self.count_filled_seen(coords=coords) < 1:
                return FieldType.TAKEN
            else:
                return FieldType.EMPTY
            pass
        else:
            return FieldType.FLOOR
        pass

    def update_grid(self) -> bool:
        new_seats = dict()
        for seat_coord in self.seats.keys():
            new_seats[seat_coord] = self.check_seat(seat_coord)
            pass

        is_equal = True
        for c in self.seats.keys():
            if not new_seats.get(c) == self.seats.get(c):
                is_equal = False
                break
            pass

        self.seats = new_seats
        return is_equal

    def update_grid2(self) -> bool:
        new_seats = dict()
        for seat_coord in self.seats.keys():
            new_seats[seat_coord] = self.check_seat2(seat_coord)
            pass

        is_equal = True
        for c in self.seats.keys():
            if not new_seats.get(c) == self.seats.get(c):
                is_equal = False
                break
            pass

        self.seats = new_seats
        #self.print()
        return is_equal

    def run(self):
        while not self.update_grid():
            pass
        print("After simulating humans there were", self.count_filled(), "taken seats.")
        pass

    def run2(self):
        while not self.update_grid2():
            pass
        self.print
        print("After simulating humans there were", self.count_filled(), "taken seats.")
        pass
    pass

class Day11_01(AdventDay):
    def __init__(self, input_path : str) -> None:
        lines = ""
        for line in open(input_path, "r"):
            lines += line
            pass
        self.grid = ConwaysGrid(lines)
        pass

    def do(self) -> None:
        self.grid.run()
        pass
    pass

class Day11_02(AdventDay):
    def __init__(self, input_path : str) -> None:
        lines = ""
        for line in open(input_path, "r"):
            lines += line
            pass
        self.grid = ConwaysGrid(lines)
        pass

    def do(self) -> None:
        self.grid.run2()
        pass
    pass

input_path = os.path.dirname(os.path.realpath(__file__)) + "/11-01_input.txt"
mission = Day11_01(input_path)
mission.do()
print("")
mission = Day11_02(input_path)
mission.do()