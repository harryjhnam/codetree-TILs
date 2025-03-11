N, M = map(int, input().split())
coin = list(map(int, input().split()))

# Please write your code here.
# dp[x] = min(dp[x-N1], dp[x-N2], ...) + 1
# dp[N1], dp[N2], ... = 1

dp = [-1] * (M+1)
for c in coin:
    dp[c] = 1

for x in range(1, M+1):
    if dp[x] != -1:
        continue

    candidates = []
    for c in coin:
        if 0 < x - c and dp[x-c] != -1:
            candidates.append( dp[x-c] )

    if candidates:
        dp[x] = min(candidates) + 1

print(dp[M])
