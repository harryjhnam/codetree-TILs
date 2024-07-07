from sortedcontainers import SortedSet

n, m = map(int, input().split())

s = SortedSet([int(input())])
res = 1e9
for _ in range(n-1):
    x = int(input())
    l_idx = s.bisect_left(x)
    r_idx = s.bisect_right(x)
    while l_idx >=0 or r_idx < len(s):
        if 0 <= l_idx < len(s) and abs(x - s[l_idx]) >= m:
            res = min(res, abs(x - s[l_idx]))
        if r_idx < len(s) and abs(x - s[r_idx]) >= m:
            res = min(res, abs(x - s[r_idx]))
        
        l_idx -= 1
        r_idx += 1
        
        s.add(x)

        if res == m:
            break   

if res == 1e9:
    print(-1)
else:
    print(res)