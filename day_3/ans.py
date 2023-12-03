
file = "input.txt"
dummy1 = "dummy1.txt"

def extract_nums(line: str) -> list[tuple[str, int]]:
    nums = []
    i = 0
    while (i < len(line)):
        if line[i].isdigit():
            cur_num = line[i]
            cur_index = i
            j = i + 1
            while line[j].isdigit():
                cur_num += line[j]
                j += 1
            nums.append((cur_num, cur_index))
            i = j
        i += 1
    return nums


def part1(file: str) -> int:
    ans = 0
    with open(file) as f:
        lines = f.readlines()
        for line_index, line in enumerate(lines):
            nums_in_line = extract_nums(line)
            for num, num_index in nums_in_line:
                should_add = False
                # Check for stuff before
                if (num_index != 0):
                    if (line[num_index - 1].isdigit() == False and line[num_index - 1] != "."):
                        should_add = True
                    if (line_index != 0 and (should_add == False)):
                        if lines[line_index - 1][num_index - 1].isdigit() == False and lines[line_index - 1][num_index - 1] != ".":
                            should_add = True
                    if (line_index != len(lines) - 1 and (should_add == False)):
                        if lines[line_index + 1][num_index - 1].isdigit() == False and lines[line_index + 1][num_index - 1] != ".":
                            should_add = True
                
                #check for stuff after
                if (num_index + len(num) != len(line) - 1 and (should_add == False)):
                    if (line[num_index + len(num)].isdigit() == False and line[num_index + len(num)] != "."):
                        should_add = True
                    if (line_index != 0 and (should_add == False)):
                        if lines[line_index - 1][num_index + len(num)].isdigit() == False and lines[line_index - 1][num_index + len(num)] != ".":
                            should_add = True
                    if (line_index != len(lines) - 1 and (should_add == False)):
                        if lines[line_index + 1][num_index + len(num)].isdigit() == False and lines[line_index + 1][num_index + len(num)] != ".":
                            should_add = True

                #check for stuff above
                if (line_index != 0 and (should_add == False)):
                    prev_line = lines[line_index - 1]
                    i = num_index
                    while i < num_index + len(num):
                        if prev_line[i].isdigit() == False and prev_line[i] != ".":
                            should_add = True
                            break
                        i += 1
                
                #check for stuff below
                if (line_index != len(lines) - 1 and (should_add == False)):
                    next_line = lines[line_index + 1]
                    i = num_index
                    while i < num_index + len(num):
                        if next_line[i].isdigit() == False and next_line[i] != ".":
                            should_add = True
                            break
                        i += 1
                
                if (should_add):
                    ans += int(num)
    return ans



def part2(file:str) -> int:
    ans = 0
    with open(file) as f:
        lines = f.readlines()
        for line_index, line in enumerate(lines):
            for char_index, c in enumerate(line):
                if c == "*":
                    surrounding_nums = []
                    nums_in_line = extract_nums(line)
                    for num, num_index in nums_in_line:
                        if num_index - 1 == char_index:
                            surrounding_nums.append(int(num))
                        if num_index + len(num) == char_index:
                            surrounding_nums.append(int(num))
                    if (line_index != 0):
                        nums_above_line = extract_nums(lines[line_index - 1])
                        for num, num_index in nums_above_line:
                            if num_index <= char_index <= num_index + len(num):
                                surrounding_nums.append(int(num))
                            if num_index == char_index + 1:
                                surrounding_nums.append(int(num))
                    if (line_index != len(lines) - 1):
                        nums_below_line = extract_nums(lines[line_index + 1])
                        for num, num_index in nums_below_line:
                            if num_index <= char_index <= num_index + len(num):
                                surrounding_nums.append(int(num))
                            if num_index == char_index + 1:
                                surrounding_nums.append(int(num))
                    if (len(surrounding_nums) == 2):
                        gear_ratio = surrounding_nums[0] * surrounding_nums[1]
                        ans += gear_ratio
    return ans


ans1 = part1(file)
print(f"part1: {ans1}")
ans2 = part2(file)
print(f"part2: {ans2}")