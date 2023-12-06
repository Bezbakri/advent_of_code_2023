file = "input.txt"
dummy1 = "dummy1.txt"

#yes, I could've used math

def part1(file: str) -> int:
    ans = 1
    with open(file) as f:
        lines = f.readlines()
        times = [int(i) for i in lines[0].split(":")[1].split()]
        distances = [int(i) for i in lines[1].split(":")[1].split()]
        for i, time in enumerate(times):
            possible_combos = 0
            req_dist = distances[i]
            for i in range(time):
                charge_time = i
                run_time = time - i
                distance_moved = charge_time * run_time
                if distance_moved > req_dist:
                    possible_combos += 1
            ans *= possible_combos
        
    return ans

def part1_optim(file: str) -> int:
    ans = 1
    with open(file) as f:
        lines = f.readlines()
        times = [int(i) for i in lines[0].split(":")[1].split()]
        distances = [int(i) for i in lines[1].split(":")[1].split()]
        for i, time in enumerate(times):
            req_dist = distances[i]
            start_range = (time + (time**2 - 4 * req_dist)**(1/2))/2
            end_range = (time - (time**2 - 4 * req_dist)**(1/2))/2    
            ans =  ans * (int(start_range) - int(end_range)) if int(start_range) + int(end_range) != time else ans * (int(start_range) - int(end_range) - 1)
        
    return ans

def part2_optim(file: str) -> int:
    ans = 1
    with open(file) as f:
        lines = f.readlines()
        time = int("".join(lines[0].split(":")[1].split()))
        req_distance = int("".join(lines[1].split(":")[1].split()))
        
        start_range = (time + (time**2 - 4 * req_distance)**(1/2))/2
        end_range = (time - (time**2 - 4 * req_distance)**(1/2))/2    
        ans =  int(start_range) - int(end_range) if int(start_range) + int(end_range) != time else int(start_range) - int(end_range) - 1
        
    return ans

def part2(file: str) -> int:
    ans = 0
    with open(file) as f:
        lines = f.readlines()
        time = int("".join(lines[0].split(":")[1].split()))
        req_distance = int("".join(lines[1].split(":")[1].split()))
        for i in range(time):
            charge_time = i
            run_time = time - i
            distance_moved = charge_time * run_time
            if distance_moved > req_distance:
                ans += 1
    return ans

# ans1 = part1(file)
# print(f"part1: {ans1}")
ans1_optim = part1_optim(file)
print(f"part1 optim: {ans1_optim}")
# ans2 = part2(file)
# print(f"part2: {ans2}")
ans2_optim = part2_optim(file)
print(f"part2 optim: {ans2_optim}")