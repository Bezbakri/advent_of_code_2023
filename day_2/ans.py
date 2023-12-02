
file = "input.txt"
dummy = "dummy1.txt"

def part1(file: str) -> int:
    id_sum = 0
    max_red = 12; max_green = 13; max_blue = 14
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            split_line = line.split()
            id = int(split_line[1][:-1])
            good_game = True
            game = line.split(":")[1].split(";")
            for trial in game:
                cube_dict = {"red": 0, "green": 0, "blue": 0}
                trial = trial.replace(",", "")
                stuff = trial.split()
                for i in range(1, len(stuff), 2):
                    cube_dict[stuff[i]] += int(stuff[i-1])
                if cube_dict["red"] > max_red or cube_dict["green"] > max_green or cube_dict["blue"] > max_blue:
                    good_game = False
            if (good_game):
                id_sum += id
            
    return id_sum

def part2(file: str) -> int:
    balls_sum = 0
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            game = line.split(":")[1].split(";")
            cube_dict = {"red": 0, "green": 0, "blue": 0}
            for trial in game:
                trial = trial.replace(",", "")
                stuff = trial.split()
                for i in range(1, len(stuff), 2):
                    if cube_dict[stuff[i]] < int(stuff[i-1]):
                        cube_dict[stuff[i]] = int(stuff[i-1])
            power = 1
            for v in cube_dict.values():
                power *= v
            balls_sum += power
    return balls_sum

ans1 = part1(file)
print(ans1)

ans2 = part2(file)
print(ans2)