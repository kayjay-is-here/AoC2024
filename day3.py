import numpy as np
import re

with open("inputs/day3.txt", "r") as f:
    contents = f.read()

def process_instructions(string):
    pattern = r"mul\(([\d]+),([\d]+)\)"
    matches = re.findall(pattern, string)
    results = []
    for match in matches:
        LHS, RHS = map(int, match)
        results.append(LHS*RHS)

    return results

def process_three_instructions(string):
    results = []
    enabled = True
    #print(re.findall(r"(do|don't)\(\)", string))
    pattern = r"(do|don't)\(\)|mul\(([\d]+),([\d]+)\)"
    for match in re.finditer(pattern, string):
        #print(f"found match {match}")
        if match.group(1):  # Check for "do" or "don't"
            if match.group(1) == "don't":
                enabled = False
            elif match.group(1) == "do":
                enabled = True
        elif enabled and match.group(2) and match.group(3):
            x, y = int(match.group(2)), int(match.group(3))
            results.append(x * y)
    return results
    
#print(process_instructions(contents))

def part_a(string):
    return sum(process_instructions(string))

def part_b(string):
    return sum(process_three_instructions(string))

print(part_a(contents))
print(part_b(contents))