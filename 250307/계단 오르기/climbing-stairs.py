n = int(input())

# Please write your code here.
# f(n) = (f(n-2) + f(n-3)) % 10_007
# f(1) = 0, f(2) = 1, f(3) = 1

memo = [-1] * (n+1)

def f(n):
    global memo

    if n <= 1:
        memo[n] = 0
        return memo[n]

    if n == 2 or n == 3:
        memo[n] = 1
        return memo[n]
    
    if memo[n] != -1:
        return memo[n]
    else:
        memo[n] = (f(n-2) + f(n-3)) % 10_007
        return memo[n]

    return memo[n]

print(f(n))

