from adventofcode import AdventDay
from enum import Enum
import os

def manhatten_distance(position):
    (x,y) = position
    if x < 0:
        x = -x
        pass
    if y < 0:
        y = -y
        pass
    return x + y

class Direction(Enum):
    NORTH = (0,1)
    EAST = (1,0)
    SOUTH = (0,-1)
    WEST = (-1,0)

    def __mul__(self, other):
        if isinstance(other, int):
            x, y = self.value
            return (x * other, y * other)
        else:
            raise Exception("Can only multiply int with Direction")
        pass

    def __rmul__(self, other):
        return self.__mul__(other)

    def turn_right_once(self):
        if self == Direction.NORTH:
            return Direction.EAST
        elif self == Direction.EAST:
            return Direction.SOUTH
        elif self == Direction.SOUTH:
            return Direction.WEST
        else:
            return Direction.NORTH
    pass

class Ship:
    def __init__(self, start_direction=Direction.EAST, start_position=(0,0)):
        self.position = start_position
        self.direction = start_direction
        pass

    def move(self, direction : Direction, distance : int) -> None:
        (dx,dy) = distance * direction
        (x,y) = self.position
        self.position = (dx + x, dy + y)
        pass

    def turn(self, degree, invert=False) -> None:
        rotations = int(degree/90)
        neg = 0
        if invert:
            neg = -1
        else:
            neg = 1
        for _ in range((neg * rotations) % 4):
            self.direction = self.direction.turn_right_once()
            pass
        pass

    def forward(self, distance) -> None:
        self.move(self.direction, distance)
        pass

    def get_manhatten_distance(self):
        return manhatten_distance(self.position)
    pass

class Day12_01(AdventDay):
    def __init__(self, input_path : str) -> None:
        self.navigation_list = list()
        self.ship = Ship()
        for line in open(input_path, "r"):
            line = line.strip()
            if not line == "":
                self.navigation_list.append((line[:1],int(line[1:])))
                pass
            pass
        pass

    def do(self) -> None:
        for i, n in self.navigation_list:
            if i == "N":
                self.ship.move(Direction.NORTH, n)
                pass
            elif i == "S":
                self.ship.move(Direction.SOUTH, n)
                pass
            elif i == "E":
                self.ship.move(Direction.EAST, n)
                pass
            elif i == "W":
                self.ship.move(Direction.WEST, n)
                pass
            elif i == "L":
                self.ship.turn(n,invert=True)
                pass
            elif i == "R":
                self.ship.turn(n)
                pass
            elif i in ["F"]:
                self.ship.forward(n)
                pass
            else:
                raise Exception("Line did not contain navigational instructions.")
            pass
        print(self.ship.get_manhatten_distance())
        pass
    pass

class Marker:
    def __init__(self):
        self.ship = (0,0)
        self.waypoint = (10,1)
        pass

    def move_waypoint(self, vector):
        self.waypoint = (self.waypoint[0]+vector[0], self.waypoint[1]+vector[1])
        pass

    def turn_waypoint(self):
        self.waypoint = (self.ship[0]+self.waypoint[1]-self.ship[1],\
                         self.ship[1]-(self.waypoint[0]-self.ship[0]))
        pass

    def move_ship(self, distance = 1):
        tmp_waypoint = (self.waypoint[0]-self.ship[0], self.waypoint[1]-self.ship[1])
        self.ship = (self.ship[0]+tmp_waypoint[0]*distance,self.ship[1]+tmp_waypoint[1]*distance)
        self.move_waypoint(vector=(tmp_waypoint[0]*distance,tmp_waypoint[1]*distance))
        pass
    pass

class Day12_02(AdventDay):
    def __init__(self, input_path : str) -> None:
        self.navigation_list = list()
        self.marker = Marker()
        for line in open(input_path, "r"):
            line = line.strip()
            if not line == "":
                self.navigation_list.append((line[:1],int(line[1:])))
                pass
            pass
        pass

    def do(self) -> None:
        for i, n in self.navigation_list:
            if i == "N":
                self.marker.move_waypoint((0,n))
                pass
            elif i == "S":
                self.marker.move_waypoint((0,-n))
                pass
            elif i == "E":
                self.marker.move_waypoint((n,0))
                pass
            elif i == "W":
                self.marker.move_waypoint((-n,0))
                pass
            elif i == "L":
                for _ in range(int(n/90)):
                    for _ in range(3):
                        self.marker.turn_waypoint()
                        pass
                    pass
                pass
            elif i == "R":
                for _ in range(int(n/90)):
                    self.marker.turn_waypoint()
                    pass
                pass
            elif i in ["F"]:
                self.marker.move_ship(n)
                pass
            else:
                raise Exception("Line did not contain navigational instructions.")
            pass
        print(manhatten_distance(self.marker.ship))
        pass
    pass

input_path = os.path.dirname(os.path.realpath(__file__)) + "/12-01_input.txt"
mission = Day12_01(input_path)
mission.do()
print("")
mission = Day12_02(input_path)
mission.do()