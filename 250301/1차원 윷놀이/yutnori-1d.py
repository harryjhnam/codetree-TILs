n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
locs = [1] * k

def count_finished():
    global locs
    score = 0
    for loc in locs:
        if loc >= m:
            score += 1
    return score


answer = 0
def make_move(n_moves):
    global answer, n, k

    if n_moves == n:
        answer = max(answer, count_finished())
        return

    for i in range(k):
        locs[i] += nums[n_moves]
        make_move(n_moves+1)
        locs[i] -= nums[n_moves]
        
    return

make_move(0)

print(answer)

