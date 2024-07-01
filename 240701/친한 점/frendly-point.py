from sortedcontainers import SortedSet

n, m = map(int, input().split())

s = SortedSet()
for _ in range(n):
    x, y = map(int, input().split())
    s.add( (x,y) )

for _ in range(m):
    x, y = map(int, input().split())
    i = s.bisect_left( (x,y) )
    if i == len(s):
        print(-1, -1)
    else:
        res = s[i]
        print(res[0], res[1])