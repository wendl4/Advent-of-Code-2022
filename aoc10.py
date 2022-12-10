def part1():
    with open('input10.txt', 'r') as input:
        cycles = 1
        register = 1
        signal_strengths = []
        for line in input:
            if cycles in [20,60,100,140,180,220]:
                signal_strengths.append(register*cycles)
            line = line.rstrip().split(" ")
            if line[0] == "noop":
                cycles+=1
            elif line[0] == "addx":
                if cycles+1 in [20,60,100,140,180,220]:
                    signal_strengths.append(register*(cycles+1))
                register += int(line[1])
                cycles+=2
    return sum(signal_strengths)

def print_crt(crt):
    for i in crt:
        a = "".join(i)
        print(a)

def part2():
    with open('input10.txt', 'r') as input:
        cycles = 0
        register = 1
        crt = [[],[],[],[],[],[]]
        sprite_position = 0
        for line in input:
            line = line.rstrip().split(" ")
            if line[0] == "noop":
                if abs(register - cycles%40) < 2:
                    crt[(cycles)//40].append('#')
                else:
                    crt[(cycles)//40].append('.')
                cycles+=1
            elif line[0] == "addx":
                for i in range(2):
                    if abs(register - cycles%40) < 2:
                        crt[(cycles)//40].append('#')
                    else:
                        crt[(cycles)//40].append('.')
                    cycles+=1
                register += int(line[1])
        print_crt(crt)
