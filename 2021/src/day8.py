from common import get_input
import collections

test_input = [
    'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
    'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
    'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
    'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
    'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
    'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
    'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
    'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
    'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
    'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce',
]

class SevenSegmentDisplay:
    def __init__(self):
        self.digit_map = {}
    
    def solve_mappings(self, signals):
        combos = {i:[] for i in [2,3,4,5,6,7]}
        for s in signals:
            combos[len(s)].append(s)
        eight = ''.join(sorted(combos[7][0]))
        seven = ''.join(sorted(combos[3][0]))
        four = ''.join(sorted(combos[4][0]))
        one = ''.join(sorted(combos[2][0]))
        self.digit_map[eight] = '8'
        self.digit_map[seven] = '7'
        self.digit_map[four] = '4'
        self.digit_map[one] = '1'
        # the mapping for 'a' is the segment in seven that isn't in one.
        a = seven
        for seg in one:
            a = a.replace(seg,'')
        # segment 'f' will be missing only once in the sequence (for '2')
        f = collections.Counter(''.join(signals)).most_common()[0][0]
        two = ''.join(sorted([s for s in signals if f not in s][0]))
        self.digit_map[two] = '2'
        # segment 'c' will be the remaining signal from '1' if we remove segment f
        c = one.replace(f,'')
        # segments 'b' and 'f' are missing from 2 but not from 8
        b = eight.replace(f,'')
        for seg in two:
            b = b.replace(seg,'')
        # d is what remains in 4 after removing bcf
        d = four
        for seg in [b,c,f]:
            d = d.replace(seg,'')
        # if we remove c and d from the six-segment signals, e is the only seg that appears only twice
        tmp = combos[6].copy()
        for i, sig in enumerate(tmp):
            for seg in [c,d]:
                sig = sig.replace(seg,'')
            tmp[i] = sig
        cnt = collections.Counter(''.join(tmp)).most_common()
        e = cnt[-1][0]
        # g is the last segment in eight after we remove the others
        g = eight
        for seg in [a,b,c,d,e,f]:
            g = g.replace(seg,'')
        # finish the digit map
        self.digit_map[''.join(sorted([a,b,c,e,f,g]))] = '0'
        self.digit_map[''.join(sorted([a,c,d,f,g]))] = '3'
        self.digit_map[''.join(sorted([a,b,d,f,g]))] = '5'
        self.digit_map[''.join(sorted([a,b,d,e,f,g]))] = '6'
        self.digit_map[''.join(sorted([a,b,c,d,f,g]))] = '9'
        return self
    
    def get_output(self, signals):
        digits = [self.digit_map[''.join(sorted(sig))] for sig in signals]
        val = int(''.join(digits))
        print(val)
        return val


def parse_puzzle(input):
    in_out_sets = []
    for line in input:
        inp, outp = line.split('|')
        in_out_sets.append([inp.split(),outp.split()])
    return in_out_sets

def part1(input):
    in_out_sets = parse_puzzle(input)
    number_size_mapping = {
        2:1,
        3:7,
        4:4,
        7:8
    }
    observed_digits = collections.Counter()
    for line in in_out_sets:
        for output in line[1]:
            output_size = len(output.strip())
            if output_size in number_size_mapping.keys():
                observed_digits[number_size_mapping[output_size]] += 1
    print(sum(observed_digits.values()))

def part2(input):
    in_out_sets = parse_puzzle(input)
    vals = []
    for line in in_out_sets:
        display = SevenSegmentDisplay().solve_mappings(line[0])
        vals.append(display.get_output(line[1]))
    print(sum(vals))

print('Part 1')
part1(test_input)
part1(get_input(8))

print('\nPart 2')
part2(test_input)
part2(get_input(8))
