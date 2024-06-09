n, k = map(int, input().split())
li = list(map(int, input().split()))

cnt = dict()
for i in li:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

res = 0
for n in cnt:
    if k-n in cnt:
        res += cnt[n] * cnt[k-n]

print(res//2)