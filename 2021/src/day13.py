from common import get_input

test_input = [
    '6,10',
    '0,14',
    '9,10',
    '0,3',
    '10,4',
    '4,11',
    '6,0',
    '6,12',
    '4,1',
    '0,13',
    '10,12',
    '3,4',
    '3,0',
    '8,4',
    '1,10',
    '2,14',
    '8,10',
    '9,0',
    '',
    'fold along y=7',
    'fold along x=5',
]

class TransparentSheet:
    def __init__(self, input):
        self.dots = set()
        self.folds = []
        for line in input:
            if 'fold along' in line:
                fold = line.replace('fold along ','').split('=')
                # set the orientation to the index to consider in a coordinate 
                if fold[0] == 'x':
                    fold[0] = 0
                else:
                    fold[0] = 1
                fold[1] = int(fold[1])
                self.folds.append(fold)
            elif line == '':
                continue
            else:
                # tuples are hashable while lists are not
                self.dots.add(tuple([int(i) for i in line.split(',')]))
    
    def fold(self, orientation, axis):
        dots = set()
        for coord in self.dots:
            new_coord = list(coord)
            if new_coord[orientation] > axis:
                new_coord[orientation] = axis + (axis-coord[orientation])
                #print(f'translated {coord} to {new_coord}')
            dots.add(tuple(new_coord))
        self.dots = dots
    
    def do_folds(self,count=-1):
        for line in self.folds[:count]:
            self.fold(*line)
        return self

    def print(self):
        max_x = max([x for x,y in self.dots])
        max_y = max([y for x,y in self.dots])
        print(max_x,max_y)
        grid = []
        for y in range(max_y+1):
            row = []
            for x in range(max_x+1):
                row.append(' ')
            grid.append(row)
        for x,y in self.dots:
            grid[y][x] = 'X'
        for row in grid:
            print(''.join(row))

test1 = TransparentSheet(test_input).do_folds(1)
print(len(test1.dots))
test2 = TransparentSheet(test_input)
test2.do_folds(len(test2.folds)).print()


real1 = TransparentSheet(get_input(13)).do_folds(1)
print(len(real1.dots))
real2 = TransparentSheet(get_input(13))
real2.do_folds(len(real2.folds)).print()
