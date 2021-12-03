from common import get_input

def depth_increases_with_window(windowsize=1):
    increases = 0
    inputs = [int(i) for i in get_input(1) if i.strip() != '']
    for index, _ in enumerate(inputs):
        if index < windowsize:
            continue
        current_window = inputs[index-windowsize:index]
        last_window = inputs[index-windowsize-1:index-1]
        if sum(last_window) < sum(current_window):
            increases += 1
    return increases

print(depth_increases_with_window(1))
print(depth_increases_with_window(3))
