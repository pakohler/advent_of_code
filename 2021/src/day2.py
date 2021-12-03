from common import get_input

example_input = [
    'forward 5',
    'down 5',
    'forward 8',
    'up 3',
    'down 8',
    'forward 2'
]

def get_final_coords(input):
    x, y = 0, 0
    aim = 0
    for i in input:
        direction, val = i.lower().split()
        val = int(val)
        if direction == 'forward':
            x += val
            y += val*aim
        elif direction == 'down':
            aim += val
        elif direction == 'up':
            aim -= val
    result = [x,y]
    print(result)
    return result

def get_coord_mult(input): 
    final_coords = get_final_coords(input)
    result = final_coords[0] * final_coords[1]
    print(result)
    return result

get_coord_mult(example_input)
print("\n")
get_coord_mult(get_input(2))
