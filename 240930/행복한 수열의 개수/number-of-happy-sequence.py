n, m = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

res = 0

# check rows
for i in range(n):
    
    prev = -1
    n_cont = 0

    for j in range(n):
        if prev != mat[i][j]:
            n_cont = 1
        else:
            n_cont += 1

        if n_cont == m:
            res += 1
            break
    
        prev = mat[i][j]

# check columns
for i in range(n):
    
    prev = -1
    n_cont = 0
    
    for j in range(n):
        if prev != mat[j][i]:
            n_cont = 1
        else:
            n_cont += 1

        if n_cont == m:
            res += 1
            break
    
        prev = mat[j][i]

print(res)