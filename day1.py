# Solution for https://adventofcode.com/2025/day/1

pos = 50
part1 = 0
part2 = 0

with open('aoc2025\\day1.txt') as f:
    for line in f:
        if line.startswith("L"):
            if pos == 0:
                pos += 100
            for i in range(int(line[1:])):
                pos -= 1
                if pos == 0:
                    part2 += 1
                    pos += 100
        else:
            for i in range(int(line[1:])):
                pos += 1
                if pos == 100:
                    part2 += 1
                if pos > 100:
                    pos -= 100
        if pos == 100:
            part1 += 1

print("Part 1 solution: " + str(part1))
print("Part 2 solution: " + str(part2))