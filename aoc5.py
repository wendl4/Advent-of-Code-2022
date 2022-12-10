def part1():
    with open('input5.txt', 'r') as input:
        stacks = [[] for i in range(9)]
        riadok = input.readline()
        while riadok[1] != '1':
            for i in range((len(riadok)-8)//3):
                val = riadok[i*4+1]
                if val != ' ':
                    stacks[i].insert(0,val)
            riadok = input.readline()

        input.readline() # empty line

        riadok = input.readline().strip()
        while riadok:
            command = riadok.split(' ')
            for i in range(int(command[1])):
                elem = stacks[int(command[3])-1].pop()
                stacks[int(command[5])-1].append(elem)
            riadok = input.readline().strip()
        
        res = ""
        for i in stacks:
            res+=i.pop()
        return res


def part2():
    with open('input5.txt', 'r') as input:
        stacks = [[] for i in range(9)]
        riadok = input.readline()
        while riadok[1] != '1':
            for i in range((len(riadok)-8)//3):
                val = riadok[i*4+1]
                if val != ' ':
                    stacks[i].insert(0,val)
            riadok = input.readline()

        input.readline() # empty line

        riadok = input.readline().strip()
        while riadok:
            command = riadok.split(' ')
            elems = []
            for i in range(int(command[1])):
                elems.append(stacks[int(command[3])-1].pop())
            for i in range(len(elems)):
                stacks[int(command[5])-1].append(elems.pop())
            riadok = input.readline().strip()
        
        res = ""
        for i in stacks:
            res+=i.pop()
        return res
