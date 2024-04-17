n = int(input())
seq = [0] + list(map(int, input().split()))

dp = [0] * (n+1)

for i in range(1, n+1):
    cur, prev = seq[i], seq[i-1]
    if cur > prev:
        # increasing
        dp[i] = dp[i-1] + 1
    else:
        # not increasing
        dp[i] = max([l for l, prev in zip(dp[:i], seq[:i]) if cur > prev]) + 1

print(max(dp))