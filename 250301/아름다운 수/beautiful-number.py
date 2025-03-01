n = int(input())

# Please write your code here.
answer = 0

def append_numbers(number):
    global answer

    if len(number) == n:
        answer += 1
        return 

    if len(number) > n:
        return 

    for i in range(1, n+1):
        append_numbers(number + [i]*i)

    return 

append_numbers([])

print(answer)
