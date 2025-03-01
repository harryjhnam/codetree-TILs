K, N = map(int, input().split())

# Please write your code here.
answer = []

def choose(curr_digit):
    if curr_digit == N:
        print(' '.join(list(map(str, answer))))
        return
    
    for n in range(1, K+1):
        answer.append(n)
        choose(curr_digit + 1)
        answer.pop()

    return

choose(0)
