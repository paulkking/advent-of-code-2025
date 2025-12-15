# AOC Day 2 Solution https://adventofcode.com/2025/day/3

part1 = 0
part2 = 0
with open('aoc2025\\day3.txt') as f:
    for line in f:
        line = line.strip()
        s = ""
        idx = 0

        val1 = max(int(x) for x in line[:-1]) # tens digit part 1
        part1 += max(int(x) for x in line[line.find(str(val1))+1:]) + val1 * 10 # ones digit. search between tens digit and rest of line

        for i in range(12):
            if i == 11: # Special case for last value; slicing end at -11 + 11 will cause an error
                val2 = max(int(x) for x in line[idx:])
            else:
                val2 = max(int(x) for x in line[idx:(-11+i)]) # Find highest value between last highest value and leave room for final digits
            idx = line[idx:].find(str(val2)) + 1 + idx # Index of last highest value
            s = s + str(val2)
        part2 += int(s)

print("Part 1 solution: " + str(part1))
print("Part 2 solution: " + str(part2))