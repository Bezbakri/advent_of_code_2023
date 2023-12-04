import queue

file = "input.txt"
dummy1 = "dummy1.txt"

def parse_winning_numbers(line: str) -> list[int]:
    ans = [int(i) for i in line.split(":")[1].split("|")[0].split()]
    return ans

def parse_our_numbers(line: str) -> list[int]:
    ans = [int(i) for i in line.split(":")[1].split("|")[1].split()]
    return ans

def part1(file: str) -> int:
    ans = 0
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            winning_numbers = parse_winning_numbers(line)
            our_numbers = parse_our_numbers(line)
            cur_score = 0
            for num in winning_numbers:
                if num in our_numbers:
                    cur_score = 2*cur_score if cur_score > 0 else 1
            ans += cur_score
    return ans

def part2(file: str) -> int:
    ans = 0
    with open(file) as f:
        lines = f.readlines()
        q = queue.PriorityQueue()
        scores = {}
        for i in range(len(lines)):
            q.put(i)
        while (not q.empty()):
            cur_index = q.get()
            cur_card = lines[cur_index]
            winning_numbers = parse_winning_numbers(cur_card)
            our_numbers = parse_our_numbers(cur_card)
            cur_score = 0
            if scores.get(cur_index, -1) == -1:
                for num in winning_numbers:
                    if num in our_numbers:
                        cur_score += 1
                scores[cur_index] = cur_score
            else:
                cur_score = scores[cur_index]
            for i in range(1, cur_score + 1):
                if (cur_index + i) >= len(lines):
                    break
                q.put(cur_index + i)
            ans += 1
    return ans

ans1 = part1(file)
print(f"part1: {ans1}")

ans2 = part2(file)
print(f"part2: {ans2}")