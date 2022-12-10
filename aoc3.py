
def part1():
    with open('input3.txt', 'r') as input:
        acc = 0
        for line in input:
            line = line.rstrip()
            half = len(line)//2
            first = set(list(line[:half]))
            second = set(list(line[half:]))
            inter = first.intersection(second)
            if len(inter) == 1:
                inter = inter.pop()
            else:
                print('error')
            if ord(inter) >= 65 and ord(inter) <= 90:
                acc += ord(inter)- (65-27)
            if ord(inter) >= 97 and ord(inter) <= 122:
                acc += ord(inter)- 96
        return acc

def part2():
    with open('input3.txt', 'r') as input:
        acc = 0
        while True:
            riadok1 = set(list(input.readline().rstrip()))
            if not riadok1:
                break
            riadok2 = set(list(input.readline().rstrip()))
            if not riadok2:
                break
            riadok3 = set(list(input.readline().rstrip()))
            if not riadok3:
                break
            inter = riadok1.intersection(riadok2)
            inter = inter.intersection(riadok3)
            if len(inter) == 1:
                inter = inter.pop()
            else:
                print('error')
            if ord(inter) >= 65 and ord(inter) <= 90:
                acc += ord(inter)- (65-27)
            if ord(inter) >= 97 and ord(inter) <= 122:
                acc += ord(inter)- 96
        return acc
