def part1():
    with open('input6.txt', 'r') as input:
        chars = input.readline()
        for i in range(4,len(chars)):
            part = chars[i-4:i]
            set_part = set(part)
            if len(set_part) == len(part):
                return i


def part2():
    with open('input6.txt', 'r') as input:
        chars = input.readline()
        for i in range(14,len(chars)):
            part = chars[i-14:i]
            set_part = set(part)
            if len(set_part) == len(part):
                return i