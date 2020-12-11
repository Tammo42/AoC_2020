import os
from adventofcode import AdventDay

class ProgLine:
    def __init__(self, cmd, arg, exe=False):
        self.cmd = cmd
        self.arg = arg
        self.exe = exe
        pass

    def set_executed(self, exe=True):
        self.exe = exe
        pass
    pass

class ProgRunner:
    def __call__(self, *args, **kwargs):
        print("Called", self.__class__.__name__)
        pass

    def __init__(self, program, start_line=0, accumulator=0):
        self.position = start_line
        self.program = program
        self.accumulator = accumulator
        pass

    def get_current_line(self):
        return self.program[self.position]

    def execute_line(self, line : ProgLine):
        line.set_executed()
        cmd = line.cmd
        if cmd == "acc":
            self.accumulator += line.arg
            self.position += 1
            pass
        elif cmd == "jmp":
            self.position += line.arg
            pass
        else:
            self.position += 1
            pass
        pass
    
    def step(self):
        self.execute_line(self.get_current_line())
        pass

    def step_unless_repeat(self) -> bool:
        executed = self.get_current_line().exe
        if not executed:
            self.step()
            return True
        else:
            return False
        pass

    def run(self):
        while self.position >= 0 and self.position < len(self.program):
            self.step()
            pass
        pass

    def run_until_repeat(self):
        while self.step_unless_repeat() \
                and self.position >= 0 and self.position < len(self.program):
            pass
        print("acc", self.accumulator)
        pass
    pass

class Day08_01(AdventDay):
    def __init__(self, input_path : str) -> None:
        self.program = []
        for line in open(input_path, "r"):
            line = line.strip()
            [cmd,arg] = line.split(" ", 1)
            self.program.append(ProgLine(cmd,int(arg)))
            pass
        pass

    def do(self) -> None:
        p = ProgRunner(self.program)
        p.run_until_repeat()
        pass
    pass

class Day08_02(AdventDay):
    def __init__(self, input_path : str) -> None:
        self.program = []
        for line in open(input_path, "r"):
            line = line.strip()
            [cmd,arg] = line.split(" ", 1)
            self.program.append(ProgLine(cmd,int(arg)))
            pass
        pass

    def replace_line(self, line_num, instr):
        self.program[line_num].cmd = instr
        pass

    def do(self) -> None:
        p = ProgRunner(self.program)
        p.run_until_repeat()
        pass
    pass



input_path = os.path.dirname(os.path.realpath(__file__)) + "/08-01_input.txt"
mission = Day08_01(input_path)
mission.do()
print("")
mission = Day08_02(input_path)
mission.do()