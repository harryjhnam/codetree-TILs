n, m = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

def is_in_mat(i, j):
    global n, m
    return (0<=i<n) and (0<=j<m)


def get_blocks(i, j):
    blocks = []

    # block 1
    blocks.append( [(i, j), (i-1, j), (i, j+1)] )
    blocks.append( [(i, j), (i+1, j), (i, j+1)] )
    blocks.append( [(i, j), (i, j-1), (i+1, j)] )
    blocks.append( [(i, j), (i, j-1), (i-1, j)] )

    # block 2
    blocks.append( [(i, j), (i, j+1), (i, j+2)] )
    blocks.append( [(i, j), (i+1, j), (i+2, j)] )

    return blocks


res = 0
for i in range(n):
    for j in range(m):
        blocks = get_blocks(i, j)
        for block in blocks:
            s = 0
            for (i,j) in block:
                if not is_in_mat(i, j):
                    s = -1
                    break
                s += mat[i][j]
            res = max(res, s)
              
print(res)