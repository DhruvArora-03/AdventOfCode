from sys import prefix
from typing import Counter


curr, prev, count = 0, 0, -1

with open("day1_input.txt", "r") as f:
    for line in f:
        curr = int(line)
        if curr > prev:
            count += 1
        prev = curr

print(count)
        