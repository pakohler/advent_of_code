from common import get_input

test_input = [
    '5483143223',
    '2745854711',
    '5264556173',
    '6141336146',
    '6357385478',
    '4167524645',
    '2176841721',
    '6882881134',
    '4846848554',
    '5283751526',
]

class Dumboctopus:
    def __init__(self, energy):
        self.energy = energy
        self.flashed = False
    
    def charge(self):
        self.energy += 1
        if self.energy == 10:
            self.flashed = True
            return True
        return False
    
    def reset(self):
        if self.flashed:
            self.flashed = False
            self.energy = 0

class Dumboctopod:
    def __init__(self, input):
        self.pod = [[Dumboctopus(int(i)) for i in line] for line in input]
        self.grid_size = 10
        self.flash_count = 0
        self.tick_count = 0
        self.tick_flashes = 0
    
    def is_valid_coord(self,x,y):
        if x < 0 or x >= self.grid_size:
            return False
        if y < 0 or y >= self.grid_size:
            return False
        return True
        
    def neighbours(self, x, y):
        return [coord for coord in [
            (x-1,y),
            (x-1,y-1),
            (x-1,y+1),
            (x,y-1),
            (x,y+1),
            (x+1,y),
            (x+1,y-1),
            (x+1,y+1)
        ] if self.is_valid_coord(*coord)]
    
    def flash_neighbours(self,x,y):
        for n in self.neighbours(x,y):
            self.charge_octopus(*n)

    def charge_octopus(self,x,y):
        if self.pod[y][x].charge():
            self.flash_neighbours(x,y)
            self.flash_count += 1
            self.tick_flashes += 1
    
    def tick(self):
        self.tick_count += 1
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                self.charge_octopus(x,y)
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                self.pod[y][x].reset()
        if self.tick_flashes == 100:
            return True
        self.tick_flashes = 0
        return False
    
    def multitick(self,count):
        for c in range(count):
            self.tick()
            #self.display()
        return self
    
    def display(self):
        for row in self.pod:
            print(''.join([str(octo.energy) for octo in row]))
        print()
    
    def find_simultaneous_flash(self):
        while not self.tick():
            pass
        return self

test = Dumboctopod(test_input).multitick(100)
print(test.flash_count)
test = Dumboctopod(test_input).find_simultaneous_flash()
print(test.tick_count)

real = Dumboctopod(get_input(11)).multitick(100)
print(real.flash_count)
real = Dumboctopod(get_input(11)).find_simultaneous_flash()
print(real.tick_count)

