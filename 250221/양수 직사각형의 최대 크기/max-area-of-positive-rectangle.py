n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
def is_including_negative(grid, row_min, row_max, col_min, col_max):
    for i in range(row_min, row_max+1):
        for j in range(col_min, col_max+1):
            if grid[i][j] <= 0:
                return True
    return False

def get_rectangle_size(row_min, row_max, col_min, col_max):
    return (row_max-row_min+1) * (col_max-col_min+1)

answer = -1
for row_min in range(n):
    for col_min in range(m):
        for row_max in range(n):
            for col_max in range(m):
                if is_including_negative(grid, row_min, row_max, col_min, col_max):
                    continue
                answer = max(answer, get_rectangle_size(row_min, row_max, col_min, col_max))

print(answer)
