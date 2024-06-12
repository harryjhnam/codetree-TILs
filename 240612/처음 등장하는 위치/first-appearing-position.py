from sortedcontainers import SortedDict

n = int(input())
li = list(map(int, input().split()))

sd = SortedDict()
for i, n in enumerate(li):
    if n not in sd:
        sd[n] = i+1

for n, idx in sd.items():
    print(f"{n} {idx}")