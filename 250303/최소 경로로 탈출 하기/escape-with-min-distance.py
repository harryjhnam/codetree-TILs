n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

visited = [[0]*m for _ in range(m)]

def is_valid(i, j):
    global n, m, grid, visited
    if not (0<=i<n and 0<=j<n):
        return False
    if visited[i][j]:
        return False
    if grid[i][j] == 0:
        return False
    return True

def dfs():
    global n, m, visited

    dis = [0,0,1,-1]
    djs = [1,-1,0,0]
    
    visited[0][0] = 1
    q = deque( [(0,0,0)] )
    while q:
        steps, curr_i, curr_j = q.popleft()
        
        if (curr_i, curr_j) == (n-1, m-1):
            return steps

        for di, dj in zip(dis, djs):
            next_i = curr_i + di
            next_j = curr_j + dj
            if is_valid(next_i, next_j):
                visited[next_i][next_j] = 1
                q.append( (steps + 1, next_i, next_j) )

    return -1


print(dfs())

