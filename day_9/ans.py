file = "input.txt"
dummy1 = "dummy1.txt"

def get_next_value(nums: list[int]) -> int:
    diffs = []
    for i in range(len(nums) - 1):
        diffs.append(nums[i+1] - nums[i])
    should_recurse = False
    for diff in diffs:
        if diff != 0:
            should_recurse = True
    if (should_recurse):
        return get_next_value(diffs) + nums[-1]
    return nums[-1]

def part1(file: str) -> int:
    ans =  0
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            nums = [int(i) for i in line.split()]
            ans += (get_next_value(nums))
    return ans

def part2(file: str) -> int:
    ans =  0
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            nums = [int(i) for i in line.split()]
            nums.reverse()
            ans += (get_next_value(nums))
    return ans

ans1 = part1(file)
print(f"part1: {ans1}")
ans2 = part2(file)
print(f"part2: {ans2}")