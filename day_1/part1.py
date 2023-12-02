

file = "input.txt"

def part1(file: str) -> int:

    ans = 0

    with open(file) as f:
        lines = f.readlines()
        
        for line in lines:
            num = ""
            for c in line:
                if c.isdigit():
                    num += c
                    break
            for c in reversed(line):
                if c.isdigit():
                    num += c
                    break

            int_num = int(num)
            ans += int_num

        
    return ans

def part2(file: str) -> int:
    ans = 0
    dict_of_nums = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "zero":0}
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            string = ""
            first_dig = None
            last_dig = None
            for c in line:
                if c.isdigit():
                    last_dig = c
                else:
                    string += c
                    for k, v in dict_of_nums.items():
                        if string.endswith(k):
                            last_dig = str(v)
                if last_dig is not None:
                    if first_dig is None:
                        first_dig = last_dig
            ans += int(first_dig + last_dig)
            
    return ans


ans2 = part2(file)
print(ans2)