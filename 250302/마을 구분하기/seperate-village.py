n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

visited = [[0]*n for _ in range(n)]
people_cnt = 0
cnts = []

def is_in_range(v):
    global n
    return 0<=v[0]<n and 0<=v[1]<n

def is_wall(v):
    global grid
    return grid[v[0]][v[1]] == 0

def dfs(v):
    global people_cnt
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    
    for d in range(4):
        next_v = (v[0]+di[d], v[1]+dj[d])
        if not is_in_range(next_v):
            continue
        if is_wall(next_v):
            continue
        if not visited[next_v[0]][next_v[1]]:
            visited[next_v[0]][next_v[1]] = 1
            people_cnt += 1
            dfs(next_v)

for i in range(n):
    for j in range(n):
        if grid[i][j] and not visited[i][j]:
            visited[i][j] = 1
            people_cnt = 1
            dfs((i, j))
            cnts.append(people_cnt)

print(len(cnts))
for cnt in sorted(cnts):
    print(cnt)
        
