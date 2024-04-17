n = int(input())
seq = [0] + list(map(int, input().split()))

dp = [0] * (n+1)

for i in range(1, n+1):
    cur, prev = seq[i], seq[i-1]
    dp[i] = max([l for l, prv in zip(dp[:i], seq[:i]) if cur > prv]) + 1

print(max(dp))