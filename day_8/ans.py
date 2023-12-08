from math import gcd

file = "input.txt"
dummy1 = "dummy1.txt"
dummy2 = "dummy2.txt"
dummy3 = "dummy3.txt"

def part1(file: str) -> int:
    ans = 0
    with open(file) as f:
        lines = f.readlines()
        instructions = lines[0].strip()
        instructions_size = len(instructions)
        stuff = lines[2:]
        the_map = {}
        for line in stuff:
            slightly_parsed = line.strip().split(" = ")
            start = slightly_parsed[0]
            left, right = slightly_parsed[1].lstrip("(").rstrip(")").split(", ")
            the_map[start] = (left, right)
        curr = "AAA"
        while curr != "ZZZ":
            curr_instruction = instructions[ans % instructions_size]
            curr = the_map[curr][0] if curr_instruction == "L" else the_map[curr][1]
            ans += 1
    return ans

def part2(file: str) -> int:
    ans_list = []
    with open(file) as f:
        lines = f.readlines()
        instructions = lines[0].strip()
        instructions_size = len(instructions)
        stuff = lines[2:]
        the_map = {}
        start_list = []
        
        for line in stuff:
            slightly_parsed = line.strip().split(" = ")
            start = slightly_parsed[0]
            left, right = slightly_parsed[1].lstrip("(").rstrip(")").split(", ")
            if start[-1] == "A":
                start_list.append(start)
            the_map[start] = (left, right)
        for elem in start_list :
            curr = elem
            index = 0
            while curr[-1] != "Z":
                curr_instruction = instructions[index % instructions_size]
                curr = the_map[curr][0] if curr_instruction == "L" else the_map[curr][1]
                index += 1
            ans_list.append(index)
    ans = 1
    for i in ans_list:
        ans = ans * i//gcd(ans, i)
    return ans

ans1 = part1(file)
print(f"part1: {ans1}")
ans2 = part2(file)
print(f"part2: {ans2}")