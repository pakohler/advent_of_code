from common import get_input

test_input = [
    '[({(<(())[]>[[{[]{<()<>>',
    '[(()[<>])]({[<{<<[]>>(',
    '{([(<{}[<>[]}>{[]{[(<()>',
    '(((({<>}<{<{<>}{[]{[]{}',
    '[[<[([]))<([[{}[[()]]]',
    '[{[{({}]{}}([{[{{{}}([]',
    '{<[[]]>}<{[{[{[]{()[[[]',
    '[<(<(<(<{}))><([]([]()',
    '<{([([[(<>()){}]>(<<{{',
    '<{([{{}}[<[[[<>{}]]]>[]]'
]

class SyntaxChecker:
    def __init__(self, input):
        self.syntax_lines = input
        self.syntax_pairs = {
            ')':'(',
            ']':'[',
            '>':'<',
            '}':'{'
        }
        self.error_values = {
            ')':3,
            ']':57,
            '}':1197,   
            '>':25137
        }
        self.completion_values = {
            '(':1,
            '[':2,
            '{':3,
            '<':4
        }
        pass

    def check_syntax(self, line):
        chunks = []
        for char in line:
            if char in self.syntax_pairs.values():
                chunks.append(char)
            elif self.syntax_pairs[char] == chunks[-1]:
                chunks.pop()
            else:
                # return syntax error as a string
                return char
        # return incomplete line as a list
        return chunks
    
    def parse_lines(self):
        return [self.check_syntax(line) for line in self.syntax_lines]
    
    def autocomplete(self, line):
        score = 0
        for char in reversed(line):
            score = score * 5
            score += self.completion_values[char]
        return score

    def part1(self):
        values = [self.error_values[line] for line in self.parse_lines() if isinstance(line, str)]
        print(sum(values))
    
    def part2(self):
        values = sorted([self.autocomplete(line) for line in self.parse_lines() if isinstance(line, list)])
        print(values[int(len(values)/2)])

test = SyntaxChecker(test_input)
test.part1()
test.part2()
real = SyntaxChecker(get_input(10))
real.part1()
real.part2()
