aim, x, y = 0, 0, 0

with open('day2_input.txt', 'r') as f:
    for line in f:
        direction, distance = line.split(' ', maxsplit=1)
        distance = int(distance)
        if (direction == 'forward'):
            x += distance
            y += aim * distance
        elif (direction == 'up'):
            aim -= distance
        else:
            aim += distance
    
print(x * y)
