N = int(input())

# Please write your code here.
# f(n) = f(n-1) + f(n-2), n >= 1
# f(1) = 1, f(2) = 1

memo = [-1] * (N+1)
memo[1] = 1
memo[2] = 1

def fibo(n):
    global memo

    if memo[n] != -1:
        return memo[n]

    memo[n] = fibo(n-1) + fibo(n-2)

    return memo[n]

print(fibo(N))


