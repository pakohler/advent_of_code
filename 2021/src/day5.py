import collections
from common import get_input
from collections import Counter

test_input = [
    '0,9 -> 5,9',
    '8,0 -> 0,8',
    '9,4 -> 3,4',
    '2,2 -> 2,1',
    '7,0 -> 7,4',
    '6,4 -> 2,0',
    '0,9 -> 2,9',
    '3,4 -> 1,4',
    '0,0 -> 8,8',
    '5,5 -> 8,2',
]

def count_points(input):
    vent_coords = collections.Counter()
    for line in input:
        start, end = [[int(i) for i in coord.split(',')] for coord in line.split(' -> ')]
        if is_horizontal(start,end):
            for i in range(min(start[0],end[0]),max(start[0],end[0])+1):
                vent_coords['{x},{y}'.format(x=i, y=start[1])] += 1
        elif is_vertical(start,end):
            for i in range(min(start[1],end[1]),max(start[1],end[1])+1):
                vent_coords['{x},{y}'.format(x=start[0],y=i)] += 1
        else:
            h_factor = horizontal_direction(start,end)
            v_factor = vertical_direction(start,end)
            x_coords = [i for i in range(start[0],end[0]+h_factor,h_factor)]
            y_coords = [i for i in range(start[1],end[1]+v_factor,v_factor)]
            for i in range(len(x_coords)):
                vent_coords['{x},{y}'.format(x=x_coords[i],y=y_coords[i])] += 1
    return len([k for k in vent_coords.keys() if vent_coords[k] >= 2])

def is_horizontal(start,end):
    return start[1] == end[1]

def is_vertical(start,end):
    return start[0] == end[0]

def vertical_direction(start,end):
    if start[1] < end[1]:
        return 1
    else:
        return -1

def horizontal_direction(start,end):
    if start[0] < end[0]:
        return 1
    else:
        return -1

print(count_points(test_input))
print(count_points(get_input(5)))
