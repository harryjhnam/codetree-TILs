from sortedcontainers import SortedSet

n = int(input())
nx_s = list(map(int, input().split()))

li = SortedSet([0])
res = 1e9
for nx in nx_s:
    r_idx = min( li.bisect_right(nx), len(li) - 1 )
    l_idx = max( r_idx - 1, 0 )
    res = min( res, abs(nx-li[r_idx]), abs(nx-li[l_idx]) )
    li.add(nx)
    print(res)