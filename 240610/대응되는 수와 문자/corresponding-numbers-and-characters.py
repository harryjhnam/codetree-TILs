n, m = map(int, input().split())
s2i = dict()
i2s = dict()
for i in range(n):
    s = input()
    s2i[s] = i+1
    i2s[i+1] = s
for _ in range(m):
    q = input()
    if q in s2i:
        print(s2i[q])
    else:
        print(i2s[int(q)])