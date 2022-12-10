config = {
    'A': {
        'X': 3,
        'Y': 6,
        'Z': 0
    },
    'B': {
        'X': 0,
        'Y': 3,
        'Z': 6
    },
    'C': {
        'X': 6,
        'Y': 0,
        'Z': 3
    }
}

points = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

def part1():
    with open('input2.txt', 'r') as input:
        acc = 0

        for line in input:
            elf_choice, my_choice = line.rstrip().split(' ')
            acc += config[elf_choice][my_choice] + points[my_choice]
        return acc


config2 = {
    'A': {
        'X': 3,
        'Y': 4,
        'Z': 8
    },
    'B': {
        'X': 1,
        'Y': 5,
        'Z': 9
    },
    'C': {
        'X': 2,
        'Y': 6,
        'Z': 7
    }
}

def part2():
    with open('input2.txt', 'r') as input:
        acc = 0

        for line in input:
            elf_choice, result = line.rstrip().split(' ')
            acc += config2[elf_choice][result]
        return acc