n = int(input())
x2y = {}
for _ in range(n):
    x, y = map(int, input().split())
    if x in x2y:
        x2y[x] = min(x2y[x], y)
    else:
        x2y[x] = y
    
res = sum(x2y.values())
print(res)