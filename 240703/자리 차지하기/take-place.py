from sortedcontainers import SortedSet

n, m = map(int, input().split())
li = list(map(int, input().split()))

empty = SortedSet(range(m)) # {0, 1, ..., m-1}
res = 0
for i in li:
    pos = empty.bisect_left(i) - 1
    if pos < 0 or not empty:
        break
    
    empty.remove(empty[pos])
    res += 1
    
print(res)