n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
import copy

def deploy_bomb(i, j):
    global n, grid
    new_grid = copy.deepcopy(grid)
    bomb_size = new_grid[i][j]
    for x in range(bomb_size):
        # horizontal
        if j+x < n:
            new_grid[i][j+x] = 0
        if j-x >= 0:
            new_grid[i][j-x] = 0
        # vertical
        if i+x < n:
            new_grid[i+x][j] = 0
        if i-x >= 0:
            new_grid[i-x][j] = 0
    return new_grid

def apply_gravity(grid):
    global n
    for i in range(n-1, 0, -1):
        for j in range(n):
            if grid[i][j] == 0:
                grid[i][j], grid[i-1][j] = grid[i-1][j], 0
    return grid

def count_tuples(grid):
    res = 0
    # horizontal
    for i in range(n):
        for j in range(n-1):
            if grid[i][j] == 0:
                continue
            if grid[i][j] == grid[i][j+1]:
                res += 1
    # vertical
    for i in range(n-1):
        for j in range(n):
            if grid[i][j] == 0:
                continue
            if grid[i][j] == grid[i+1][j]:
                res += 1
    return res

# def pretty_print(grid):
#     for row in grid:
#         print(' '.join(list(map(str, row))))
#     print()
#     return None

answer = 0
for bomb_i in range(n):
    for bomb_j in range(n):
        new_grid = deploy_bomb(bomb_i, bomb_j)
        new_grid = apply_gravity(new_grid)
        tuple_count = count_tuples(new_grid)
        answer = max(answer, tuple_count)

print(answer)

