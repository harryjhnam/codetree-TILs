N, M = map(int, input().split())

# Please write your code here.
numbers = [0]

def print_numbers():
    global numbers
    print(' '.join(list(map(str, numbers[1:]))))

def append_number():
    global numbers

    if len(numbers) == M+1:
        print_numbers()
        return

    for i in range(numbers[-1]+1, N+1):
        numbers.append(i)
        append_number()
        numbers.pop()

    return

append_number()
