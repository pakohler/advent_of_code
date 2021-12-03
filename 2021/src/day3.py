from common import get_input

test_data = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010',
]

def parse_diag_report(input):
    length = len(input[0].strip())
    bit_frequency = {i:[0,0] for i in range(length)}
    for binary in input:
        for index, bit in enumerate(binary.strip()):
            val = int(bit)
            bit_frequency[index][val] += 1
    return bit_frequency

def get_gamma_and_epsilon(input):
    bit_frequency = parse_diag_report(input)
    length = len(input[0].strip())
    gamma = ''
    epsilon = ''
    for i in range(length):
        maxi = str(bit_frequency[i].index(max(bit_frequency[i])))
        mini = str(bit_frequency[i].index(min(bit_frequency[i])))
        gamma += maxi
        epsilon += mini
    print('gamma',gamma, int(gamma,2))
    print('epsil', epsilon, int(epsilon,2))
    print('power.consumption', int(gamma,2)*int(epsilon,2))

def get_oxy_and_co2(input):
    oxy, co2 = input.copy(), input.copy()
    oxy_index, co2_index = 0,0
    while len(oxy) > 1:
        bit_frequency = parse_diag_report(oxy)
        maxi = str(bit_frequency[oxy_index].index(max(bit_frequency[oxy_index])))
        if bit_frequency[oxy_index][0] == bit_frequency[oxy_index][1]:
            maxi = '1'
        oxy = [i for i in oxy if i[oxy_index] == maxi]
        oxy_index += 1
    while len(co2) > 1:
        bit_frequency = parse_diag_report(co2)
        mini = str(bit_frequency[co2_index].index(min(bit_frequency[co2_index])))
        if bit_frequency[co2_index][0] == bit_frequency[co2_index][1]:
            mini = '0'
        co2 = [i for i in co2 if i[co2_index] == mini]
        co2_index += 1
    oxy = oxy[0].strip()    
    co2 = co2[0].strip()
    print('oxy', oxy, int(oxy,2))
    print('co2', co2, int(co2,2))
    print('life.support', int(oxy,2) * int(co2,2))

def run_tests(input):
    get_gamma_and_epsilon(input)
    print()
    get_oxy_and_co2(input)

run_tests(test_data)
print("\n")
run_tests(get_input(3))
