from common import get_input

test_input = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7'''

class BingoBoard:
    def __init__(self, boardstr):
        self.rows = [[int(c) for c in row.split()] for row in boardstr.split('\n')]
        self.numbers = {}
        self.solved = False
        for row_index, row in enumerate(self.rows):
            for column_index, num in enumerate(row):
                self.numbers[num] = {
                    'row': row_index, 
                    'col': column_index
                }

    def dab(self, number):
        if self.solved:
            return 0
        if number not in self.numbers.keys():
            return 0
        row,col = self.numbers[number]['row'], self.numbers[number]['col']
        self.rows[row][col] = 0
        return self.is_solved(number)

    def is_solved(self, number):
        for row in self.rows:
            if sum(row) == 0:
                return self.score(number)
        for col in range(5):
            if sum([r[col] for r in self.rows]) == 0:
                return self.score(number)
        return 0

    def score(self, number):
        self.solved = True
        return sum([sum(r) for r in self.rows]) * number


def parse_input(input):
    lines = input.split('\n')
    called_numbers = [int(n) for n in lines[0].split(',')]
    boards = [l for l in lines[1:] if l.strip() != '']
    boards = [boards[i:i+5] for i in range(0, len(boards), 5)]
    boards = [BingoBoard('\n'.join(b)) for b in boards]
    return [called_numbers, boards]


def solve(input):
    called_numbers, boards = parse_input(input)
    winners = []
    for n in called_numbers:
        for b in boards:
            res = b.dab(n)
            if res > 0:
                winners.append(res)
    print('first winner score:', winners[0])
    print('last winner score: ', winners[-1])

solve(test_input)
solve('\n'.join(get_input(4)))