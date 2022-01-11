vals = [0, 0, 0]
i = 0
count = 0

with open("day1_input.txt", "r") as f:
    for line in f:
        if vals[-1] != 0 and vals[i] < int(line):
            count += 1
        vals[i] = int(line)
        i = (i + 1) % 3

print(count)