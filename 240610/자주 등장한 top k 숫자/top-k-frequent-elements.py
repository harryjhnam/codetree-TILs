from collections import Counter

n, k = map(int, input().split())
li = list(map(int, input().split()))
cnt = Counter(li)

topk = sorted(cnt.items(), key=lambda x: (x[1], x[0]), reverse=True)[:k]
for i, c in topk:
    print(i, end=' ')