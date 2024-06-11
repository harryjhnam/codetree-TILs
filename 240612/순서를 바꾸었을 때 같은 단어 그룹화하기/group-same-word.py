from collections import defaultdict

n = int(input())

cnt = defaultdict(int)
for _ in range(n):
    cnt[''.join(sorted(input()))] += 1
print(max(list(cnt.values())))