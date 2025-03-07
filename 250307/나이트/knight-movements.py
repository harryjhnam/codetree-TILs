n = int(input())
r1, c1, r2, c2 = map(int, input().split())

# Please write your code here.
from collections import deque

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1


visited = [[0]*n for _ in range(n)]
visited[r1][c1] = 1

q = deque( [(r1, c1, 0)] )

def is_valid(r, c):
    global visited, n
    if not ( 0<=r<n and 0<=c<n ):
        return False
    if visited[r][c]:
        return False
    return True

def dfs(q):
    global visited, r2, c2
    
    dis = [-1, -2, -2, -1, 1, 2, 2, 1]
    djs = [-2, -1, 1, 2, 2, 1, -1, -2]

    while q:
        r, c, n_moves = q.popleft()
        if r == r2 and c == c2:
            return n_moves
        
        for di, dj in zip(dis, djs):
            nr, nc = r + di, c + dj
            if is_valid(nr, nc):
                visited[nr][nc] = 1
                q.append( (nr, nc, n_moves+1) )

    return -1

print(dfs(q))