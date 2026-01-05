# part 1 solution
import re

ops = [[] for _ in range(1000)]

with open('aoc2025\\day6.txt') as f:
    for line in f:
        line = re.split(r'\s+',line.strip())
        for i in range(len(line)):
            ops[i].append(line[i])

def calc(op):
    op[0:4] = [int(n) for n in op[0:4]]
    if op[-1] == "*":
        return op[0] * op[1] * op[2] * op[3]
    elif op[-1] == "+":
        return op[0] + op[1] + op[2] + op[3]
    return 0

part1 = sum([calc(op) for op in ops])

# part 2

import re

f=open('aoc2025\\day6.txt')
lines=f.readlines()
ops2 = re.split(r'\s+',lines[4].strip())
nums = [[] for _ in range(len(lines[0])-1)]

for line in lines[:-1]:
    for i in range(len(line)-1):
        nums[i].append(line[i])

idx = 0
part2 = 0
stack = []

for i in range(len(nums)):
    if nums[i] == [' ',' ',' ',' ']: # calculate
        if ops2[idx] == "*":
            calc = 1
            for n in stack:
                calc *= n
            part2 += calc
        elif ops2[idx] == "+":
            for n in stack:
                part2 += n
        stack = []
        idx += 1
    else:
        
        num = int(''.join(nums[i]).strip())
        stack.append(num)

if ops2[idx] == "*":
    calc = 1
    for n in stack:
        calc *= n
    part2 += calc
elif ops2[idx] == "+":
    for n in stack:
        part2 += n
stack = []
idx += 1

print("Part 1 solution: " + str(part1))
print("Part 2 solution: " + str(part2))