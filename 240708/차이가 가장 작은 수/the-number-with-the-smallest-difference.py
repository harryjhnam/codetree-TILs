from sortedcontainers import SortedSet

n, m = map(int, input().split())
s = SortedSet([int(input()) for _ in range(n)])

res = 1e9
for x in s:
    min_idx = s.bisect_left(x+m)
    if min_idx < len(s):
        res = min(res, s[min_idx] - x)
    max_idx = s.bisect_left(x-m) - 1
    if max_idx >= 0:
        res = min(res, x - s[max_idx])
    
    if res == m:
        break

if res == 1e9:
    print(-1)
else:
    print(res)