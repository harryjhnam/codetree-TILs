n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

def is_valid(v):
    global n, m, grid, visited
    i, j = v
    if not (0<=i<n and 0<=j<m):
        return False
    if visited[i][j]:
        return False
    if grid[i][j] == 0:
        return False
    return True

def bfs(q, visited):

    dis = [0, 0, 1, -1]
    djs = [1, -1, 0, 0]

    while q:
        curr_v = q.popleft()
        if curr_v == (n-1, m-1):
            return 1

        for di, dj in zip(dis, djs):
            next_v = (curr_v[0]+di, curr_v[1]+dj)
            if is_valid(next_v):
                visited[next_v[0]][next_v[1]] = 1
                q.append(next_v)

    return 0

visited = [[0]*m for _ in range(n)]
visited[0][0] = 1
q = deque([(0,0)])
print(bfs(q, visited))