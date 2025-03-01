n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
locs = [0] * k
answer = 0
def make_move(n_moves):
    global locs, nums, answer
    
    answer = max(answer, len([loc for loc in locs if loc >= m-1]))

    if n_moves == n:
        return

    for i in range(k):
        if locs[i] >= m:
            continue
        locs[i] += nums[n_moves]
        make_move(n_moves + 1)
        locs[i] -= nums[n_moves]

make_move(0)
print(answer)
