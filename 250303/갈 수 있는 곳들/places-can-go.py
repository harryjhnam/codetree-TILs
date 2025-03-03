n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
from collections import deque

answer = 0
visited = [[0]*n for _ in range(n)]

def is_valid(v):
    global n, visited, grid
    i, j = v
    if not (0<=i<n and 0<=j<n):
        return False
    if visited[i][j]:
        return False
    if grid[i][j] == 1:
        return False
    return True

def dfs(q):
    global visited

    dis = [0,0,1,-1]
    djs = [1,-1,0,0]

    while q:
        curr_v = q.popleft()
        for di, dj in zip(dis, djs):
            next_v = (curr_v[0]+di, curr_v[1]+dj)
            if is_valid(next_v):
                visited[next_v[0]][next_v[1]] = 1
                q.append(next_v)

for point in points:
    point = (point[0]-1, point[1]-1)

    if visited[point[0]][point[1]]:
        continue

    visited[point[0]][point[1]] = 1
    q = deque([point])
    dfs(q)

print(sum([sum(row) for row in visited]))