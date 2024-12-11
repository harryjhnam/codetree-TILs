n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

def get_rectangles(start_i, start_j):
    global n, mat

    def _is_in_mat(i, j):
        return 0<=i<n and 0<=j<n

    def _get_dir(d, i, j, steps_in_dir1, steps_in_dir2):
        n_locs = steps_in_dir1 if d in [1, 3] else steps_in_dir2
        di = [0, -1, -1, +1, +1]
        dj = [0, +1, -1, -1, +1]
        locs = []
        while True:
            if not _is_in_mat(i, j):
                break
            locs.append( (i, j) )
            i, j = i + di[d], j + dj[d]
            if len(locs) == n_locs:
                break
        i, j = i - di[d], j - dj[d]
        return locs, i, j

    res = []

    max_steps_in_dir1 = n - start_j
    for steps_in_dir1 in range(1, max_steps_in_dir1 + 1):

        max_steps_in_dir2 = (start_i + 1) - steps_in_dir1 + 1

        # TODO: 직사각형이 아닌 대각선형으로 나오는 경우에 대한 예외 처리
        if max_steps_in_dir2 == 1:
            continue
        if max_steps_in_dir1 == 1:
            max_steps_in_dir2 = 1

        for steps_in_dir2 in range(1, max_steps_in_dir2 + 1):

            i, j = start_i, start_j
            locs = []
            for d in range(1, 5):
                dir_locs, i, j = _get_dir(d, i, j, steps_in_dir1, steps_in_dir2)
                locs += dir_locs
                if i == start_i and j == start_j:
                    break
            locs = list(set(locs))
            res.append(locs)
    
    return res

ans = 0
for start_i in range(n):
    for start_j in range(n):
        for rec in get_rectangles(start_i, start_j):
            score = 0
            for i, j in rec:
                score += mat[i][j]
            ans = max(ans, score)

print(ans)

# for rec in get_rectangles(2, 1):
#     locs_mat = [[0]*n for _ in range(n)]
#     for i, j in rec:
#         locs_mat[i][j] = 1
#     for r in locs_mat:
#         print(r)
#     print()
