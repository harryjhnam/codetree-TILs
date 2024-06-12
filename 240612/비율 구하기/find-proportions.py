from sortedcontainers import SortedDict

n = int(input())
sd = SortedDict()
for _ in range(n):
    s = input()
    if s in sd:
        sd[s] += 1
    else:
        sd[s] = 1

for k, v in sd.items():
    print(f"{k} {round(v/n*100, 4):0.4f}")