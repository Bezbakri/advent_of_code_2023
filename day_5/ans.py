file = "input.txt"
dummy1 = "dummy1.txt"

def parse_seeds(raw_seeds: str) -> list[int]:
    return [int(i) for i in raw_seeds.split(" ")[1:]]

def parse_seeds_part2(raw_seeds: str) -> list[tuple[int]]:
    seeds_ranges = []
    data = raw_seeds.split(" ")[1:]
    for i in range(0, len(data), 2):
        start = int(data[i])
        end = int(data[i + 1])
        seeds_ranges.append((start, start + end - 1))
    return seeds_ranges

class Seed_to_soil_map:
    def __init__(self) -> None:
        self.maps = {}
        self.breakpoints = set()
    def parse_seed_to_soil_map(self, raw_input: str) -> None:
        lines = raw_input.split("\n")[1:]
        for line in lines:
            data = line.split()
            start = int(data[1])
            self.maps[start] = (int(data[2]), int(data[0]) - start)
            self.breakpoints.add(start)
            self.breakpoints.add(int(data[2]) + start)
    def get_soil(self, seed: int) -> int:
        for k, v in self.maps.items():
            if k <= seed < v[0] + k:
                return seed + v[1]
        return seed
    def get_soil_ranges(self, seed_ranges: list[tuple[int]]) -> list[tuple[int]]:
        soil_ranges = []
        for seed_range in seed_ranges:
            broken_range = False
            locs = set()
            start = seed_range[0]
            end = seed_range[1]
            locs.add(start)
            locs.add(end)
            for breaking in self.breakpoints:
                if start < breaking <= end:
                    locs.add(breaking - 1)
                    locs.add(breaking)
            locs = sorted(locs)
            for i in range(0, len(locs), 2):
                new_range = None
                if (i + 1 != len(locs)):
                    new_range = (self.get_soil(locs[i]), self.get_soil(locs[i + 1]))
                else:
                    new_range = (self.get_soil(locs[i]), self.get_soil(locs[i]))
                soil_ranges.append(new_range)
        return soil_ranges
    


class Soil_to_fertilizer_map:
    def __init__(self) -> None:
        self.maps = {}
        self.breakpoints = set()
    def parse_soil_to_fertilizer_map(self, raw_input: str) -> None:
        lines = raw_input.split("\n")[1:]
        for line in lines:
            data = line.split()
            start = int(data[1])
            self.maps[start] = (int(data[2]), int(data[0]) - start)
            self.breakpoints.add(start)
            self.breakpoints.add(int(data[2]) + start)
    def get_fertilizer(self, soil: int) -> int:
        for k, v in self.maps.items():
            if k <= soil < v[0] + k:
                return soil + v[1]
        return soil  
    def get_fertilizer_ranges(self, soil_ranges: list[tuple[int]]) -> list[tuple[int]]:
        fertilizer_ranges = []
        for soil_range in soil_ranges:
            broken_range = False
            locs = set()
            start = soil_range[0]
            end = soil_range[1]
            locs.add(start)
            locs.add(end)
            for breaking in self.breakpoints:
                if start < breaking <= end:
                    locs.add(breaking - 1)
                    locs.add(breaking)
            locs = sorted(locs)
            for i in range(0, len(locs), 2):
                new_range = None
                if (i + 1 != len(locs)):
                    new_range = (self.get_fertilizer(locs[i]), self.get_fertilizer(locs[i + 1]))
                else:
                    new_range = (self.get_fertilizer(locs[i]), self.get_fertilizer(locs[i]))
                fertilizer_ranges.append(new_range)
        return fertilizer_ranges

class Fertilizer_to_water_map:
    def __init__(self) -> None:
        self.maps = {}
        self.breakpoints = set()
    def parse_fertilizer_to_water_map(self, raw_input: str) -> None:
        lines = raw_input.split("\n")[1:]
        for line in lines:
            data = line.split()
            start = int(data[1])
            self.maps[start] = (int(data[2]), int(data[0]) - start)
            self.breakpoints.add(start)
            self.breakpoints.add(int(data[2]) + start)
    def get_water(self, fertilizer: int) -> int:
        for k, v in self.maps.items():
            if k <= fertilizer < v[0] + k:
                return fertilizer + v[1]
        return fertilizer
    def get_water_ranges(self, fertilizer_ranges: list[tuple[int]]) -> list[tuple[int]]:
        water_ranges = []
        for fertilizer_range in fertilizer_ranges:
            broken_range = False
            locs = set()
            start = fertilizer_range[0]
            end = fertilizer_range[1]
            locs.add(start)
            locs.add(end)
            for breaking in self.breakpoints:
                if start < breaking <= end:
                    locs.add(breaking - 1)
                    locs.add(breaking)
            locs = sorted(locs)
            for i in range(0, len(locs), 2):
                new_range = None
                if (i + 1 != len(locs)):
                    new_range = (self.get_water(locs[i]), self.get_water(locs[i + 1]))
                else:
                    new_range = (self.get_water(locs[i]), self.get_water(locs[i]))
                water_ranges.append(new_range)
        return water_ranges

class Water_to_light_map:
    def __init__(self) -> None:
        self.maps = {}
        self.breakpoints = set()
    def parse_water_to_light_map(self, raw_input: str) -> None:
        lines = raw_input.split("\n")[1:]
        for line in lines:
            data = line.split()
            start = int(data[1])
            self.maps[start] = (int(data[2]), int(data[0]) - start)
            self.breakpoints.add(start)
            self.breakpoints.add(int(data[2]) + start)
    def get_light(self, water: int) -> int:
        for k, v in self.maps.items():
            if k <= water < v[0] + k:
                return water + v[1]
        return water   
    def get_light_ranges(self, water_ranges: list[tuple[int]]) -> list[tuple[int]]:
        light_ranges = []
        for water_range in water_ranges:
            broken_range = False
            locs = set()
            start = water_range[0]
            end = water_range[1]
            locs.add(start)
            locs.add(end)
            for breaking in self.breakpoints:
                if start < breaking <= end:
                    locs.add(breaking - 1)
                    locs.add(breaking)
            locs = sorted(locs)
            for i in range(0, len(locs), 2):
                new_range = None
                if (i + 1 != len(locs)):
                    new_range = (self.get_light(locs[i]), self.get_light(locs[i + 1]))
                else:
                    new_range = (self.get_light(locs[i]), self.get_light(locs[i]))
                light_ranges.append(new_range)
        return light_ranges

class Light_to_temperature_map:
    def __init__(self) -> None:
        self.maps = {}
        self.breakpoints = set()
    def parse_light_to_temperature_map(self, raw_input: str) -> None:
        lines = raw_input.split("\n")[1:]
        for line in lines:
            data = line.split()
            start = int(data[1])
            self.maps[start] = (int(data[2]), int(data[0]) - start)
            self.breakpoints.add(start)
            self.breakpoints.add(int(data[2]) + start)
    def get_temp(self, light: int) -> int:
        for k, v in self.maps.items():
            if k <= light < v[0] + k:
                return light + v[1]
        return light  
    def get_temp_ranges(self, light_ranges: list[tuple[int]]) -> list[tuple[int]]:
        temp_ranges = []
        for light_range in light_ranges:
            broken_range = False
            locs = set()
            start = light_range[0]
            end = light_range[1]
            locs.add(start)
            locs.add(end)
            for breaking in self.breakpoints:
                if start < breaking <= end:
                    locs.add(breaking - 1)
                    locs.add(breaking)
            locs = sorted(locs)
            for i in range(0, len(locs), 2):
                new_range = None
                if (i + 1 != len(locs)):
                    new_range = (self.get_temp(locs[i]), self.get_temp(locs[i + 1]))
                else:
                    new_range = (self.get_temp(locs[i]), self.get_temp(locs[i]))
                temp_ranges.append(new_range)
        return temp_ranges     

class Temperature_to_humidity_map:
    def __init__(self) -> None:
        self.maps = {}
        self.breakpoints = set()
    def parse_temperature_to_humidity_map(self, raw_input: str) -> None:
        lines = raw_input.split("\n")[1:]
        for line in lines:
            data = line.split()
            start = int(data[1])
            self.maps[start] = (int(data[2]), int(data[0]) - start)
            self.breakpoints.add(start)
            self.breakpoints.add(int(data[2]) + start)
    def get_humidity(self, temp: int) -> int:
        for k, v in self.maps.items():
            if k <= temp < v[0] + k:
                return temp + v[1]
        return temp   
    def get_humidity_ranges(self, temp_ranges: list[tuple[int]]) -> list[tuple[int]]:
        humidity_ranges = []
        for temp_range in temp_ranges:
            broken_range = False
            locs = set()
            start = temp_range[0]
            end = temp_range[1]
            locs.add(start)
            locs.add(end)
            for breaking in self.breakpoints:
                if start < breaking <= end:
                    locs.add(breaking - 1)
                    locs.add(breaking)
            locs = sorted(locs)
            for i in range(0, len(locs), 2):
                new_range = None
                if (i + 1 != len(locs)):
                    new_range = (self.get_humidity(locs[i]), self.get_humidity(locs[i + 1]))
                else:
                    new_range = (self.get_humidity(locs[i]), self.get_humidity(locs[i]))
                humidity_ranges.append(new_range)
        return humidity_ranges  

class Humidity_to_location_map:
    def __init__(self) -> None:
        self.maps = {}
        self.breakpoints = set()
    def parse_humidity_to_location_map(self, raw_input: str) -> None:
        lines = raw_input.split("\n")[1:]
        for line in lines:
            data = line.split()
            if (len(data) == 0):
                continue
            start = int(data[1])
            self.maps[start] = (int(data[2]), int(data[0]) - start)
            self.breakpoints.add(start)
            self.breakpoints.add(int(data[2]) + start)
    def get_loc(self, humidity: int) -> int:
        for k, v in self.maps.items():
            if k <= humidity < v[0] + k:
                return humidity + v[1]
        return humidity    
    def get_loc_ranges(self, humidity_ranges: list[tuple[int]]) -> list[tuple[int]]:
        loc_ranges = []
        for humidity_range in humidity_ranges:
            broken_range = False
            locs = set()
            start = humidity_range[0]
            end = humidity_range[1]
            locs.add(start)
            locs.add(end)
            for breaking in self.breakpoints:
                if start < breaking <= end:
                    locs.add(breaking - 1)
                    locs.add(breaking)
            locs = sorted(locs)
            for i in range(0, len(locs), 2):
                new_range = None
                if (i + 1 != len(locs)):
                    new_range = (self.get_loc(locs[i]), self.get_loc(locs[i + 1]))
                else:
                    new_range = (self.get_loc(locs[i]), self.get_loc(locs[i]))
                loc_ranges.append(new_range)
        return loc_ranges         

def part1(file: str) -> int:
    ans = 0
    with open(file) as f:
        raw_data = f.read()
        sections = raw_data.split("\n\n")
        seeds = parse_seeds(sections[0])
        seed_to_soil_map = Seed_to_soil_map()
        seed_to_soil_map.parse_seed_to_soil_map(sections[1])
        soils = []
        for seed in seeds:
            soils.append(seed_to_soil_map.get_soil(seed))
        soil_to_fertilizer_map = Soil_to_fertilizer_map()
        soil_to_fertilizer_map.parse_soil_to_fertilizer_map(sections[2])
        fertilizers = []
        for soil in soils:
            fertilizers.append(soil_to_fertilizer_map.get_fertilizer(soil))
        fertilizer_to_water_map = Fertilizer_to_water_map()
        fertilizer_to_water_map.parse_fertilizer_to_water_map(sections[3])
        waters = []
        for fertilizer in fertilizers:
            waters.append(fertilizer_to_water_map.get_water(fertilizer))
        water_to_light_map = Water_to_light_map()
        water_to_light_map.parse_water_to_light_map(sections[4])
        lights = []
        for water in waters:
            lights.append(water_to_light_map.get_light(water))
        light_to_temperature_map = Light_to_temperature_map()
        light_to_temperature_map.parse_light_to_temperature_map(sections[5])
        temps = []
        for light in lights:
            temps.append(light_to_temperature_map.get_temp(light))
        temperature_to_humidity_map = Temperature_to_humidity_map()
        temperature_to_humidity_map.parse_temperature_to_humidity_map(sections[6])
        humidities = []
        for temp in temps:
            humidities.append(temperature_to_humidity_map.get_humidity(temp))
        humidity_to_location_map = Humidity_to_location_map()
        humidity_to_location_map.parse_humidity_to_location_map(sections[7])
        locs = []
        for humidity in humidities:
            locs.append(humidity_to_location_map.get_loc(humidity))
        ans = min(locs)
    return ans


def part2(file: str) -> int:
    ans = 0
    with open(file) as f:
        raw_data = f.read()
        sections = raw_data.split("\n\n")
        seed_ranges = parse_seeds_part2(sections[0])
        
        seed_to_soil_map = Seed_to_soil_map()
        seed_to_soil_map.parse_seed_to_soil_map(sections[1])
        soil_ranges = seed_to_soil_map.get_soil_ranges(seed_ranges)
        
        soil_to_fertilizer_map = Soil_to_fertilizer_map()
        soil_to_fertilizer_map.parse_soil_to_fertilizer_map(sections[2])
        fertilizer_ranges = soil_to_fertilizer_map.get_fertilizer_ranges(soil_ranges)
        
        fertilizer_to_water_map = Fertilizer_to_water_map()
        fertilizer_to_water_map.parse_fertilizer_to_water_map(sections[3])
        water_ranges = fertilizer_to_water_map.get_water_ranges(fertilizer_ranges)
        
        water_to_light_map = Water_to_light_map()
        water_to_light_map.parse_water_to_light_map(sections[4])
        light_ranges = water_to_light_map.get_light_ranges(water_ranges)
        
        light_to_temperature_map = Light_to_temperature_map()
        light_to_temperature_map.parse_light_to_temperature_map(sections[5])
        temp_ranges = light_to_temperature_map.get_temp_ranges(light_ranges)
        
        temperature_to_humidity_map = Temperature_to_humidity_map()
        temperature_to_humidity_map.parse_temperature_to_humidity_map(sections[6])
        humidity_ranges = temperature_to_humidity_map.get_humidity_ranges(temp_ranges)
   
        humidity_to_location_map = Humidity_to_location_map()
        humidity_to_location_map.parse_humidity_to_location_map(sections[7])
        loc_ranges = humidity_to_location_map.get_loc_ranges(humidity_ranges)
        ans = loc_ranges[0][0]
        for loc_range in loc_ranges:
            if loc_range[0] < ans:
                ans = loc_range[0]
    return ans

ans1 = part1(file)
print(f"part1: {ans1}")
ans2 = part2(file)
print(f"part2: {ans2}")