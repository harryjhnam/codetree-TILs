n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
answer = 0
def select(cnt, n_selected, xor_res):
    global answer

    if cnt >= n:
        if n_selected == m:
            answer = max(answer, xor_res)
        return

    select(cnt+1, n_selected+1 , xor_res ^ A[cnt])
    select(cnt+1, n_selected, xor_res)
    
    return

select(0, 0, 0)
print(answer)
