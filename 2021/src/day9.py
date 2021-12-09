from common import get_input
import itertools

test_input = [
    '2199943210',
    '3987894921',
    '9856789892',
    '8767896789',
    '9899965678',
]

class HeightMap:
    def __init__(self, input):
        self.map = [[int(i) for i in line.strip()] for line in input]
        self.max_x = len(self.map[0])
        self.max_y = len(self.map)
        self.low_points = []
        self.basins = []
    
    def height(self, x, y):
        return self.map[y][x]
    
    def is_valid_coord(self,x,y):
        if x < 0 or x >= self.max_x:
            return False
        if y < 0 or y >= self.max_y:
            return False
        return True

    def neighbours(self,x,y):
        return [c for c in [
            (x-1,y),
            (x+1,y),
            (x,y-1),
            (x,y+1)
        ] if self.is_valid_coord(*c)]

    def is_low_point(self, x, y):
        val = self.height(x,y)
        if val == 9:
            return False
        for c in self.neighbours(x,y):
            if self.height(*c) < val:
                return False
        return True
    
    def find_low_points(self):
        for x in range(self.max_x):
            for y in range(self.max_y):
                coord = (x,y)
                if self.is_low_point(*coord):
                    self.low_points.append(coord)
        return self

    def low_points_total(self):
        total = len(self.low_points)
        for c in self.low_points:
            total += self.height(*c)
        return(total)

    def flood_basin(self, low_point):
        basin_points = set()
        basin_points.add(low_point)
        while True:
            dup = basin_points.copy()
            for b in basin_points:
                for point in [n for n in self.neighbours(*b) if self.height(*n) < 9]:
                    dup.add(point)
            if len(dup) == len(basin_points):
                break
            basin_points = dup
        return basin_points
                    
    def find_basins(self):
        self.basins = [self.flood_basin(coord) for coord in self.low_points]
    
    def basin_mult(self):
        self.find_basins()
        basin_sizes = sorted([len(basin) for basin in self.basins])
        return(basin_sizes[-3]*basin_sizes[-2]*basin_sizes[-1])


test_map = HeightMap(test_input).find_low_points()
print('test_data:', test_map.low_points_total(), test_map.basin_mult())
print()
real_map = HeightMap(get_input(9)).find_low_points()
print('real_data:', real_map.low_points_total(), real_map.basin_mult())
