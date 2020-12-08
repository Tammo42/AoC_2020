import os
from functools import reduce
from adventofcode import AdventDay
from typing import List

Passport = dict

class PassportImporter:
    def __init__(self, input_path) -> None:
        self.input_path = input_path
    
    def import_passports(self) -> List[Passport]:
        passports = list()
        passport = Passport()
        counter = 0
        for line in open(self.input_path, "r"):
            line = line.rstrip()
            if line == "":
                if 0 < len(passport.keys()):
                    passports.append(passport)
                    counter += 1
                    passport = Passport()
            else:
                props = line.split()
                for prop in props:
                    prop_tmp = prop.split(":",1)
                    passport[prop_tmp[0]] = prop_tmp[1]
        passports.append(passport)
        counter += 1
        passport = Passport()
        print("Found", counter, "passports.")
        return passports

class PassportValidator:
    def __init__(self, fields=["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"] \
                , optionals=["cid"]) -> None:
        self.fields = fields
        self.optionals = optionals

    def validate_passport(self, passport) -> bool:
        valid = True
        for field in self.fields:
            if (field not in passport) and (field not in self.optionals):
                valid = False
        return valid

class Day04_01(AdventDay):
    def __init__(self, input_path) -> None:
        self.passport_importer = PassportImporter(input_path)
        self.passport_validator = PassportValidator()

    def do(self) -> None:
        counter = 0
        for passport in self.passport_importer.import_passports():
            if self.passport_validator.validate_passport(passport):
                counter += 1
        print("There were", counter, "valid passports.")

class PassportValidator2:
    def __init__(self, fields=["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"] \
                , optionals=["cid"]) -> None:
        self.fields = fields
        self.optionals = optionals

    def check_byr(self, value) -> bool:
        return len(value) == 4 \
            and 1919 < int(value) \
            and int(value) < 2003

    def check_iyr(self, value) -> bool:
        return len(value) == 4 \
            and 2009 < int(value) \
            and int(value) < 2021

    def check_eyr(self, value) -> bool:
        return len(value) == 4 \
            and 2019 < int(value) \
            and int(value) < 2031

    def check_hgt(self, value) -> bool:
        valid = True
        value.lstrip("0")
        if len(value) == 5 and value.endswith("cm"):
            num = value[:3]
            if not (num.isdecimal() \
                and 149 < int(num) \
                and int(num) < 194):
                valid = False
        elif len(value) == 4 and value.endswith("in"):
            num = value[:2]
            if not (num.isdecimal() \
                and 58 < int(num) \
                and int(num) < 77):
                valid = False
        else:
            valid = False
        return valid

    def check_hcl(self, value) -> bool:
        hex_vals = ["a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        return len(value) == 7 and value[0] == "#" \
            and reduce((lambda a, b: a and (b in hex_vals)), value[1:], True)
    
    def check_ecl(self, value) -> bool:
        valid_eyes = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return value in valid_eyes

    def check_pid(self, value) -> bool:
        return len(value) == 9 and value.isdecimal()

    def check_cid(self, value) -> bool:
        return True

    def validate_passport(self, passport) -> bool:
        valid = True
        for field in self.fields:
            if (field not in passport) and (field not in self.optionals):
                #print("Passport is missing:", field, "in", passport.keys())
                valid = False
            elif field in passport:
                if (field == "byr" and not self.check_byr(passport[field])) \
                        or (field == "iyr" and not self.check_iyr(passport[field])) \
                        or (field == "eyr" and not self.check_eyr(passport[field])) \
                        or (field == "hgt" and not self.check_hgt(passport[field])) \
                        or (field == "hcl" and not self.check_hcl(passport[field])) \
                        or (field == "ecl" and not self.check_ecl(passport[field])) \
                        or (field == "pid" and not self.check_pid(passport[field])) \
                        or (field == "cid" and not self.check_cid(passport[field])):
                    valid = False
        return valid

class Day04_02(AdventDay):
    def __init__(self, input_path) -> None:
        self.passport_importer = PassportImporter(input_path)
        self.passport_validator = PassportValidator2()

    def do(self) -> None:
        counter = 0
        for passport in self.passport_importer.import_passports():
            if self.passport_validator.validate_passport(passport):
                counter += 1
        print("There were", counter, "valid passports.")

input_path = os.path.dirname(os.path.realpath(__file__)) + "/04-01_input.txt"
mission = Day04_01(input_path)
mission.do()
print("")
mission = Day04_02(input_path)
mission.do()