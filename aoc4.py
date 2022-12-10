def part1():
    with open('input4.txt', 'r') as input:
        acc = 0
        for line in input:
            ranges = line.rstrip().split(',')
            rngs = []
            for rang in ranges:
                start,end = rang.split('-')
                rngs.append([int(start), int(end)])
            if (rngs[0][0] >= rngs[1][0] and rngs[0][1] <= rngs[1][1]) or (rngs[0][0] <= rngs[1][0] and rngs[0][1] >= rngs[1][1]):
                acc+=1

        return acc

def part2():
    with open('input4.txt', 'r') as input:
        acc = 0
        for line in input:
            ranges = line.rstrip().split(',')
            rngs = []
            for rang in ranges:
                start,end = rang.split('-')
                rngs.append([int(start), int(end)])
            if (rngs[0][0] >= rngs[1][1] and rngs[0][1] <= rngs[1][0]) or (rngs[0][0] <= rngs[1][1] and rngs[0][1] >= rngs[1][0]):
                acc+=1

        return acc
