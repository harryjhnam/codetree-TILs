n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

res = 0
for i in range(n-2):
    for j in range(n-2):
        coins = sum([sum(mat[_i][j:j+3]) for _i in range(i, i+3)])
        res = max(res, coins)

print(res)