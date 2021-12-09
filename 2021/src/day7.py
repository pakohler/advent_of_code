from common import get_input
import collections
import math
from functools import cmp_to_key

test_input = [16,1,2,0,4,2,7,1,2,14]
real_input = [int(i) for i in get_input(7)[0].split(',')]

class CrabArmada:
    def __init__(self, input):
        self.crab_positions = input
        self.crab_cluster = collections.Counter(self.crab_positions)
        self.proximity_scale = int(math.ceil((max(input)-min(input)) * 0.33))

    def fuel_cost(self, pos):
        return sum([sum(range(abs(i - pos)+1))for i in self.crab_positions])

    def nearby_crabs(self, pos):
        return sum([self.crab_cluster[i] for i in range(pos-self.proximity_scale, pos+self.proximity_scale)])

    def compare_density(self, a, b):
        loc1_nearby=self.nearby_crabs(a)
        loc2_nearby=self.nearby_crabs(b)
        return loc2_nearby - loc1_nearby
    
    def compare_fuel_cost(self,a,b):
        fuela = self.fuel_cost(a)
        fuelb = self.fuel_cost(b)
        return fuela - fuelb

    def best_position(self):
        densest_positions = sorted(
            [i for i in range(min(self.crab_positions),max(self.crab_positions)+1)],
            key=cmp_to_key(self.compare_density)
        )
        highest_density = self.nearby_crabs(densest_positions[0])
        current_density = highest_density
        best_positions = []
        index = 0
        while current_density >= highest_density * 0.66:
            best_positions.append(densest_positions[index])
            index += 1
            current_density = self.nearby_crabs(densest_positions[index])
        best_position = sorted(best_positions, key=cmp_to_key(self.compare_fuel_cost))[0]
        print(best_position, self.nearby_crabs(best_position), self.fuel_cost(best_position))

CrabArmada(test_input).best_position()
CrabArmada(real_input).best_position()