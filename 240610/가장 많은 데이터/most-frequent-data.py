from collections import defaultdict
n = int(input())
cnt = defaultdict(int)
M = 0
for _ in range(n):
    s = input()
    cnt[s] += 1
    M = max(M, cnt[s])
print(M)