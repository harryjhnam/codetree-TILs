from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(int)
li = list(map(int, input().split()))
for i in li:
    d[i] += 1
li = list(map(int, input().split()))
for j in li:
    print(d[j], end=' ')