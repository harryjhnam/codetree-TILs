from collections import Counter

n, k = map(int, input().split())
li = list(map(int, input().split()))

cnt = Counter()
for i in li:
    cnt[i] += 1

res = 0
for x in range(n-1):
    for y in range(x+1, n):
        cnt[li[x]] -= 1
        cnt[li[y]] -= 1
        res += cnt[ k-(li[x]+li[y]) ]
        cnt[li[x]] += 1
        cnt[li[y]] += 1

print(res//3)