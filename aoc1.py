def part1():
    with open('input.txt', 'r') as input:
        max = 0
        acc = 0
        i = 0
        for line in input:
            line = line.rstrip()
            if line == "":
                if acc > max:
                    max = acc
                acc = 0
            else:
                acc += int(line)
            i+=1

        return max


def part2():
    with open('input.txt', 'r') as input:
        acc = 0
        i = 0
        listofi = []
        for line in input:
            line = line.rstrip()
            if line == "":
                listofi.append(acc)
                acc = 0
            else:
                acc += int(line)
            i+=1

        listofi.sort(reverse=True)
        listofi = listofi[:3]
        return sum(listofi)