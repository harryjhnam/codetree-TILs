n = int(input())

# Please write your code here.
visited = [0] * (n+1)

seq = []

def print_seq():
    global seq
    for i in seq:
        print(i, end=" ")
    print()

def append_seq():
    global visited, seq

    if len(seq) == n:
        print_seq()
        return

    for i in range(n, 0, -1):
        if visited[i]:
            continue
        
        visited[i] = 1
        seq.append(i)
        
        append_seq()

        visited[i] = 0
        seq.pop()

append_seq()
