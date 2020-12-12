from adventofcode import AdventDay
from concurrent.futures import ThreadPoolExecutor
import os

class ProgLine:
    def copy(self):
        return ProgLine(self.cmd, self.arg)

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
        #print(cmd)
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
        print("The accumulator is at", self.accumulator)
        pass

    def run_until_repeat(self) -> (bool,int):
        while self.step_unless_repeat() \
                and self.position >= 0 and self.position < len(self.program):
            pass
        return (not len(self.program) == self.position, self.accumulator)
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
        (_, acc) = p.run_until_repeat()
        print("The accumulator is at", acc)
        pass
    pass

class Day08_02(AdventDay):
    def __init__(self, input_path : str) -> None:
        self.executor = ThreadPoolExecutor(8)
        self.program = []
        for line in open(input_path, "r"):
            line = line.strip()
            [cmd,arg] = line.split(" ", 1)
            self.program.append(ProgLine(cmd,int(arg)))
            pass
        pass

    def replace_line(self, program, line_num, instr):
        program[line_num].cmd = instr
        return program
    
    def program_with_replacement(self, index, instr):
        return ProgRunner(self.replace_line([l.copy() for l in self.program], index, instr))

    def do(self) -> None:
        progRunners = list()
        for index, line in enumerate(self.program):
            if line.cmd == "jmp":
                progRunners.append(self.program_with_replacement(index, "nop"))
                pass
            elif line.cmd == "nop":
                progRunners.append(self.program_with_replacement(index, "jmp"))
                pass
            else:
                pass
            pass
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures_to_p = {executor.submit(p.run_until_repeat): p for p in progRunners}
            for future in futures_to_p:
                try:
                    (interrupted, result) = future.result()
                except Exception:
                    print("An error occured.")
                    pass
                else:
                    if not interrupted:
                        print("The accumulator is at", result)
                        pass
                    pass
                pass
            pass
        pass
    pass



input_path = os.path.dirname(os.path.realpath(__file__)) + "/08-01_input.txt"
mission = Day08_01(input_path)
mission.do()
print("")
mission = Day08_02(input_path)
mission.do()