n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

visited = [[0]*n for _ in range(n)]
def is_valid(i, j):
    global n, visited
    for c in range(n):
        if visited[i][c]:
            return False
    for r in range(n):
        if visited[r][j]:
            return False
    return True

res = 0
results = []
def choose(curr_n):
    global n, res, results

    if curr_n == n:
        results.append(res)

    for i in range(n):
        for j in range(n):
            if is_valid(i, j):
                res += grid[i][j]
                visited[i][j] = 1
                choose(curr_n+1)
                res -= grid[i][j]
                visited[i][j] = 0
    

choose(0)
print(max(results))
