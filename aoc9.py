directions = {
    'R': (1,0),
    'L': (-1,0),
    'U': (0,-1),
    'D': (0,1)
}

def is_next_to(pos1,pos2):
    distance = abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])
    if distance < 2:
        return True
    elif distance == 2 and pos1[0] != pos2[0] and pos1[1] != pos2[1]:
        return True
    return False

def is_diagonal3(pos1,pos2):
    distance = abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])
    if distance == 3:
        return True
    return False

def is_diagonal3or4(pos1,pos2):
    distance = abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])
    if distance == 3 or distance == 4:
        return True
    return False

def come_closer(head,tail):
    if is_next_to(head,tail):
        return tail
    elif is_diagonal3(head,tail):
        for pos in ((tail[0]+1,tail[1]+1),(tail[0]-1,tail[1]-1),(tail[0]-1,tail[1]+1),(tail[0]+1,tail[1]-1)):
            if is_next_to(head,pos):
                return pos
    else:
        for pos in ((tail[0]+1,tail[1]),(tail[0]-1,tail[1]),(tail[0],tail[1]+1),(tail[0],tail[1]-1)):
            if is_next_to(head,pos):
                return pos
    return None

def come_closer2(head,tail):
    if is_next_to(head,tail):
        return tail
    elif is_diagonal3or4(head,tail):
        for pos in ((tail[0]+1,tail[1]+1),(tail[0]-1,tail[1]-1),(tail[0]-1,tail[1]+1),(tail[0]+1,tail[1]-1)):
            if is_next_to(head,pos):
                return pos
    else:
        for pos in ((tail[0]+1,tail[1]),(tail[0]-1,tail[1]),(tail[0],tail[1]+1),(tail[0],tail[1]-1)):
            if is_next_to(head,pos):
                return pos
    return None



def part1():
    with open('input9.txt', 'r') as input:
        positions = set()
        head=(0,0)
        tail=(0,0)
        positions.add(tail)
        for line in input:
            line = line.rstrip().split(" ")
            for i in range(int(line[1])):
                head = (head[0]+directions[line[0]][0], head[1]+directions[line[0]][1])
                tail = come_closer(head,tail)
                positions.add(tail)
    return len(positions)

def part2():
    with open('input9.txt', 'r') as input:
        positions = set()
        rope = [(0,0)]*10
        step = 1
        positions.add(rope[9])
        for line in input:
            line = line.rstrip().split(" ")
            for i in range(int(line[1])):
                rope[0] = (rope[0][0]+directions[line[0]][0], rope[0][1]+directions[line[0]][1])
                for i in range(1,10):
                    rope[i] = come_closer2(rope[i-1],rope[i])
                positions.add(rope[9])
            step+=1
    return len(positions)
