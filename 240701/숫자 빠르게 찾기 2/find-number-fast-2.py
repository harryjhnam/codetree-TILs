from sortedcontainers import SortedSet

n, m = map(int, input().split())
li = SortedSet(list(map(int, input().split())))

for _ in range(m):
    i = int(input())
    res = li.bisect_left(i)
    if res == len(li):
        print(-1)
    else:
        print(li[res])