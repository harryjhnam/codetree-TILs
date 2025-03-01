n = int(input())

# Please write your code here.
answer = 0

def append_numbers(numbers):
    global n, answer

    if len(numbers) == n:
        answer += 1
        return

    if len(numbers) > n:
        return

    for i in range(1, 5):
        append_numbers(numbers + [i]*i)
        
    return

append_numbers([])
print(answer)