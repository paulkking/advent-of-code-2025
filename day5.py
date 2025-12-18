# AOC Day 5 Solution https://adventofcode.com/2025/day/5

s = set()
part1 = 0

with open("aoc2025\\day5.txt") as f:
    ranges, ids = f.read().split("\n\n")
ranges = ranges.split("\n")
ranges = [[int(x) for x in rang.split("-")] for rang in ranges]
ids = [int(x) for x in ids.split("\n")]

def isvalid(id_): # For Part 1
    for rang in ranges: # Iterate through all ranges
        if rang[0] <= id_ and id_ <= rang[1]:
            return True
    return False

for id_ in ids:
    if isvalid(id_):
        part1 += 1

ranges.sort()

merged = [ranges[0]]
part2 = 0

for rang in ranges[1:]:
    if rang[0] > merged[-1][1]: # Add range if entirely separate from last range
        merged.append(rang)
    elif rang[1] <= merged[-1][1]: # Ignore range if entirely contained in last range
        pass
    else:
        merged[-1][1] = rang[1] # Expand range if first number is within last range and second number is after last range

for rang in merged:
    part2 += rang[1] - rang[0] + 1


print("Part 1 solution: " + str(part1))
print("Part 2 solution: " + str(part2))