n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
from copy import deepcopy

def deploy_bomb(grid, i, j):
    global n
    bomb_size = grid[i][j]
    for x in range(bomb_size):
        if j+x < n:
            grid[i][j+x] = 0
        if j-x >= 0:
            grid[i][j-x] = 0
        if i+x < n:
            grid[i+x][j] = 0
        if i-x >= 0:
            grid[i-x][j] = 0
    return grid

def apply_gravity(grid):
    global n
    for i in range(n-1, 0, -1):
        for j in range(n):
            if grid[i][j] == 0:
                grid[i][j], grid[i-1][j] = grid[i-1][j], 0
    return grid

def count_neighbors(grid):
    global n
    res = 0
    # horizontal
    for i in range(n):
        for j in range(n-1):
            if grid[i][j] != 0 and grid[i][j] == grid[i][j+1]:
                res += 1
    # vertical
    for i in range(n-1):
        for j in range(n):
            if grid[i][j] != 0 and grid[i][j] == grid[i+1][j]:
                res += 1
    return res
    
answer = 0
for i in range(n):
    for j in range(n):
        new_grid = deepcopy(grid)
        new_grid = deploy_bomb(new_grid, i, j)
        new_grid = apply_gravity(new_grid)
        res = count_neighbors(new_grid)
        answer = max(answer, res)

print(answer)