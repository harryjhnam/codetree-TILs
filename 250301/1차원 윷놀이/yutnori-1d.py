n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
locs = [0] * k
answer = 0

def calc():
    global locs
    score = 0
    for loc in locs:
        score += (loc >= m-1)
    return score

def make_move(n_moves):
    global locs, nums, answer
    
    answer = max(answer, calc())

    if n_moves == n:
        return

    for i in range(k):
        if locs[i] >= m-1:
            continue
        locs[i] += nums[n_moves]
        make_move(n_moves + 1)
        locs[i] -= nums[n_moves]

make_move(0)
print(answer)
