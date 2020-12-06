import os
from enum import Enum

class FieldType(Enum):
    FREE = 0
    TREE = 1
    PASSED = 2

class Grid:
    def __init__(self, input_path):
        self.rows = list()
        self.line_width = 0
        for line in open(input_path, "r"):
            line = line.rstrip()
            if self.line_width == 0:
                self.line_width = len(line)
            elif self.line_width != len(line):
                print("WARNING: Unstable Grid!")
            self.rows.append(line)
        self.height = len(self.rows)
    
    def getFieldType(self, width, height):
        if height < 1:
            print("You need to enter the forest, to be one with the forest.")
        if self.height <= height:
            return FieldType.PASSED
        symbol = self.rows[height][width % self.line_width]
        #print(self.rows[height])
        #spacing = ""
        #for _ in range(width % self.line_width):
            #spacing += " "
        #print(spacing + str(symbol))
        if symbol == ".":
            return FieldType.FREE
        else:
            return FieldType.TREE

class Slope:
    def __init__(self, input_path, angle_right, angle_down=1):
        self.forest = Grid(input_path)
        self.angle_right = angle_right
        self.angle_down = angle_down

    def get_trees_on_slope(self):
        tree_counter = 0
        # (width, height)
        cur_pos = (0, 0)
        while cur_pos[1] < self.forest.height:
            field_type = self.forest.getFieldType(cur_pos[0], cur_pos[1])
            if field_type == FieldType.TREE:
                tree_counter = tree_counter + 1
            cur_pos = (cur_pos[0] + self.angle_right, cur_pos[1] + self.angle_down)
        return tree_counter

class Day03_01:
    def __init__(self, input_path, angle_right, angle_down=1):
        self.slope = Slope(input_path, angle_right, angle_down)

    def do(self):
        print("Met", self.slope.get_trees_on_slope(), "trees.")

class Day03_02:
    def __init__(self, input_path, angles):
        self.slopes = list()
        for (angle_right, angle_down) in angles:
            self.slopes.append(Slope(input_path, angle_right, angle_down))

    def do(self):
        product = 1
        for slope in self.slopes:
            trees = slope.get_trees_on_slope()
            product *= trees
            print("Met", trees, "trees on the trajectory of (", slope.angle_right, ";", slope.angle_down, ").")
        print("The product is", product, ".")

input_path = os.path.dirname(os.path.realpath(__file__)) + "/03-01_input.txt"
mission = Day03_01(input_path, 3)
mission.do()
print("")
mission = Day03_02(input_path, list(((1,1),(3,1),(5,1),(7,1),(1,2))))
mission.do()