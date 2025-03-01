n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# find bomb locations
potential_bomb_locs = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            potential_bomb_locs.append( (i, j) )

# explode bombs and count bombed area
def count_bombed_area(bombs):
    global n

    bomb_types = [
        [],
        [(-2, 0), (-1, 0), (1, 0), (2, 0)],
        [(-1, 0), (1, 0), (0, -1), (0, 1)],
        [(-1, 1), (-1, -1), (1, 1), (1, -1)]
    ]

    bombed_area = [[0]*n for _ in range(n)]
    for bomb_type, (x, y) in bombs:
        bombed_area[x][y] = 1
        for bombed in bomb_types[bomb_type]:
            nx = x + bombed[0]
            ny = y + bombed[1]
            if 0<=nx<n and 0<=ny<n:
                bombed_area[nx][ny] = 1
        
    return sum([sum(row) for row in bombed_area])

# place bombs for each locations
answers = []

def place_bombs(potential_bomb_locs, bombs):
    global answers

    if not potential_bomb_locs:
        answers.append(count_bombed_area(bombs))
        return

    for bomb_type in range(1, 4):
        bomb_loc = potential_bomb_locs[0]
        place_bombs(potential_bomb_locs[1:], bombs + [(bomb_type, bomb_loc)])

    return

place_bombs(potential_bomb_locs, [])
print(max(answers))
