import os
input_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),'inputs')

def get_input(day):
    return [line.strip() for line in open(os.path.join(input_dir, f'day{day}.txt')).readlines()]
