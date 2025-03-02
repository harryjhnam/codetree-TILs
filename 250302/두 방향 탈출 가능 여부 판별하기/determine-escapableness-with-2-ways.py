n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
di = [1, 0]
dj = [0, 1]

answer = 0
visited = [[0]*m for _ in range(n)]
def dfs(curr_v):
    global di, dj, visited, answer

    if curr_v == (n-1, m-1):
        answer = 1
        return
    
    for d in range(2):
        next_v = (curr_v[0]+di[d], curr_v[1]+dj[d])

        if not (0<=next_v[0]<n and 0<=next_v[1]<m):
            # out of range
            continue
        
        if grid[next_v[0]][next_v[1]] == 0:
            # snake
            continue

        if not visited[next_v[0]][next_v[1]]:
            visited[next_v[0]][next_v[1]] = 1
            dfs(next_v)

visited[0][0] = 1
dfs((0,0))
print(answer)
