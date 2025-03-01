K, N = map(int, input().split())

# Please write your code here.
def print_numbers(numbers):
    numbers = list(map(str, numbers))
    print(' '.join(numbers))

def append_number(numbers):
    
    if len(numbers) == N:
        print_numbers(numbers)
        return

    for i in range(1, K+1):
        if len(numbers) >= 2 and numbers[-1] == numbers[-2] == i:
            continue
        append_number(numbers + [i])
    
    return

append_number([])
    