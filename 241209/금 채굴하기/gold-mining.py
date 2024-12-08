n, gold_cost = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

def get_mining_area(i, j, k):
    res = set()
    for i_range in range(k+1):
        for j_range in range(k-i_range+1):
            res.add( (i-i_range, j-j_range) )
            res.add( (i-i_range, j+j_range) )
            res.add( (i+i_range, j-j_range) )
            res.add( (i+i_range, j+j_range) )
    return list(res)

def is_valid_corr(i, j, n):
    return 0<=i<n and 0<=j<n

def is_profitable(n_golds, gold_cost, n_area):
    return (n_golds*gold_cost) >= n_area

ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n, -1, -1):
            mining_area = get_mining_area(i, j, k)
            n_area = len(mining_area)
            n_golds = 0
            for x, y in mining_area:
                if not is_valid_corr(x, y, n):
                    continue
                n_golds += mat[x][y]
            if n_golds < ans:
                break
            if is_profitable(n_golds, gold_cost, n_area):
                ans = n_golds

print(ans)

