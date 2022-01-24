x, y = 0, 0

with open('day2_input.txt', 'r') as f:
    for line in f:
        direction, distance = line.split(' ', maxsplit=1)
        distance = int(distance)
        if (direction == 'forward'):
            x += distance
        elif (direction == 'up'):
            y -= distance
        else:
            y += distance
    
print(x * y)
