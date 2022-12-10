def part1():
    with open('input8.txt', 'r') as input:
        grid = []
        for line in input:
            line = list(line.rstrip())
            line = [int(i) for i in line]
            grid.append(line)
        border_x = len(grid[0])
        border_y = len(grid)

        acc = 0
        for i in range(len(grid)): # y
            for j in range(len(grid[i])): # x
                top = i
                bottom = i
                left = j
                right = j
                if i == 0 or j==0 or j == border_x-1 or i == border_y-1:
                    acc += 1
                else:
                    visible = False
                    while top > 0:
                        top -=1
                        top_tree = grid[top][j]
                        if top_tree >= grid[i][j]:
                            break
                        if top == 0:
                            visible = True
                    if visible == False:
                        while bottom < border_y - 1:
                            bottom +=1
                            bottom_tree = grid[bottom][j]
                            if bottom_tree >= grid[i][j]:
                                break
                            if bottom == border_y - 1:
                                visible = True

                    if visible == False:
                        while left > 0:
                            left -=1
                            left_tree = grid[i][left]
                            if left_tree >= grid[i][j]:
                                break
                            if left == 0:
                                visible = True
                    if visible == False:
                        while right < border_x - 1:
                            right +=1
                            right_tree = grid[i][right]
                            if right_tree >= grid[i][j]:
                                break
                            if right == border_x - 1:
                                visible = True
                    if visible == True:
                        acc += 1
                        
        
    return acc


def part2():
    with open('input8.txt', 'r') as input:
        grid = []
        for line in input:
            line = list(line.rstrip())
            line = [int(i) for i in line]
            grid.append(line)
        border_x = len(grid[0])
        border_y = len(grid)

        acc = 0
        for i in range(len(grid)): # y
            for j in range(len(grid[i])): # x
                view_angle = 1
                top = i
                bottom = i
                left = j
                right = j
                if i == 0 or j==0 or j == border_x-1 or i == border_y-1:
                    pass
                else:
                    acc_top = 0
                    acc_bottom = 0
                    acc_left = 0
                    acc_right = 0
                    while top > 0:
                        top -=1
                        top_tree = grid[top][j]
                        acc_top += 1
                        if top_tree >= grid[i][j]:
                            break

                    while bottom < border_y - 1:
                        bottom +=1
                        bottom_tree = grid[bottom][j]
                        acc_bottom += 1
                        if bottom_tree >= grid[i][j]:
                            break

                    while left > 0:
                        left -=1
                        left_tree = grid[i][left]
                        acc_left += 1
                        if left_tree >= grid[i][j]:
                            break

                    while right < border_x - 1:
                        right +=1
                        acc_right += 1
                        right_tree = grid[i][right]
                        if right_tree >= grid[i][j]:
                            break

                    mult = acc_top * acc_right * acc_left * acc_bottom
                    if mult > acc:
                        acc = mult
        
    return acc

part2()