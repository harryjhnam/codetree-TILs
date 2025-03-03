n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
from collections import deque

def make_move(i, j):
    global n, grid

    res_i, res_j = i, j
    next_max = 0

    dis = [1,0,0,-1]
    djs = [0,1,-1,0]

    visited = [[0]*n for _ in range(n)]
    visited[i][j] = 1
    q = deque([(i, j)])
    while q:
        curr_v = q.popleft()

        for di, dj in zip(dis, djs):
            next_v = (curr_v[0]+di, curr_v[1]+dj)

            if not (0<=next_v[0]<n and 0<=next_v[1]<n):
                # out of grid
                continue
            if visited[next_v[0]][next_v[1]]:
                # visited
                continue
            if grid[next_v[0]][next_v[1]] >= grid[i][j]:
                # bigger than the starting point
                continue

            if grid[next_v[0]][next_v[1]] >= next_max:
                res_i, res_j = next_v
                next_max = grid[next_v[0]][next_v[1]]

            visited[next_v[0]][next_v[1]] = 1
            q.append(next_v)

    return res_i, res_j

r, c = r-1, c-1
for _ in range(k):
    new_r, new_c = make_move(r, c)
    if new_r == r and new_c == c:
        break
    r, c = new_r, new_c

print(r+1, c+1)
