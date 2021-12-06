from common import get_input

test_input = [3,4,3,1,2]

class School:
    def __init__(self, input):
        self.pool = {i:0 for i in range(9)}
        self.pool[-1] = 0
        for i in input:
            self.pool[i] += 1
    
    def tick(self):
        for i in range(9):
            self.pool[i-1] = self.pool[i]
        self.pool[6] += self.pool[-1]
        self.pool[8] = self.pool[-1]
        self.pool[-1] = 0
    
    def multitick(self,days):
        for i in range(days):
            self.tick()
        return self
    
    def sum(self):
        return sum(self.pool.values())

print(School(test_input).multitick(18).sum())
print(School(test_input).multitick(80).sum())
print(School(test_input).multitick(256).sum())
day6_input = [int(i) for i in get_input(6)[0].split(',')]
print(School(day6_input).multitick(80).sum())
print(School(day6_input).multitick(256).sum())
