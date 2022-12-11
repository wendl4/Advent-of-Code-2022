import math
import functools


class Monkey:

    def __init__(self):
        self.inspected = 0

def part1():
    with open('input11.txt', 'r') as input:
        monkeys = []
        for _ in range(8):
            input.readline()
            lines = []
            for _ in range(5):
                lines.append(input.readline())
            monita = Monkey()
            monita.items = list(map(lambda x: int(x), lines[0].split(":")[1].strip().split(',')))
            monita.operation = lines[1].split("=")[1].strip()
            monita.divisor = int(lines[2].strip().split(" ")[3])
            monita.if_true = int(lines[3].strip().split(" ")[5])
            monita.if_false = int(lines[4].strip().split(" ")[5])
            input.readline()
            monkeys.append(monita)

    NO_OF_ROUNDS = 20
    for round in range(NO_OF_ROUNDS):
        for monita in monkeys:
            for old in monita.items:
                item = eval(monita.operation)
                bored_divisor = 3
                item = item // bored_divisor
                if item % monita.divisor == 0:
                    monkeys[monita.if_true].items.append(item)
                else:
                    monkeys[monita.if_false].items.append(item)
                monita.inspected += 1
            monita.items = []

    return math.prod(list(reversed(sorted([monita.inspected for monita in monkeys])))[:2])



def part2():
    with open('input11.txt', 'r') as input:
        monkeys = []
        for _ in range(8):
            input.readline()
            lines = []
            for _ in range(5):
                lines.append(input.readline())
            monita = Monkey()
            monita.items = list(map(lambda x: int(x), lines[0].split(":")[1].strip().split(',')))
            operation = lines[1].split("=")[1].strip()
            monita.operator = '*' if '*' in operation else '+'
            operation_number = operation.split(monita.operator)[1].strip()
            monita.operation_number = operation_number if operation_number == 'old' else int(operation.split(monita.operator)[1].strip())
            monita.divisor = int(lines[2].strip().split(" ")[3])
            monita.if_true = int(lines[3].strip().split(" ")[5])
            monita.if_false = int(lines[4].strip().split(" ")[5])
            input.readline()
            monkeys.append(monita)

    NO_OF_ROUNDS = 10000
    bored_divisor = functools.reduce(lambda a, b: a*b, [monkey.divisor for monkey in monkeys])
    for _ in range(NO_OF_ROUNDS):
        for monita in monkeys:
            for old in monita.items:
                if monita.operation_number == 'old':
                    item = old + old if monita.operator == '+' else old * old
                else:
                    item = old + monita.operation_number if monita.operator == '+' else old * monita.operation_number
                if item > bored_divisor:
                    item = item % ((item // bored_divisor) * bored_divisor)
                if item % monita.divisor == 0:
                    monkeys[monita.if_true].items.append(item)
                else:
                    monkeys[monita.if_false].items.append(item)
                monita.inspected += 1
            monita.items = []

    return math.prod(list(reversed(sorted([monita.inspected for monita in monkeys])))[:2])