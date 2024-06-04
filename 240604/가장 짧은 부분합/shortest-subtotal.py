n, s = map(int, input().split())
li = list(map(int, input().split()))

ans = 1e9
for i in range(n):
    total = 0
    for j in range(i, n):
        total += li[j]
        if total >= s:
            ans = min(ans, j-i+1)
            break

if ans < 1e9:
    print(ans)
else:
    print(-1)