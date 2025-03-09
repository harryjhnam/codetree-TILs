n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# dp[r][c] = max(dp[r-1][c], dp[r][c-1]) + g[r][c]

dp = [[0]*n for _ in range(n)]
temp_sum = 0
for r in range(n):
    temp_sum += grid[r][0]
    dp[r][0] = temp_sum
temp_sum = 0
for c in range(n):
    temp_sum += grid[0][c]
    dp[0][c] = temp_sum

for r in range(1, n):
    for c in range(1, n):
        dp[r][c] = max(dp[r-1][c], dp[r][c-1]) + grid[r][c]

print(dp[n-1][n-1])
