n = int(input())

# Please write your code here.
visited = [0] * (n+1)

seq = []

def print_seqeunce():
    global seq
    for i in seq:
        print(i, end=" ")
    print()

def append_seq():
    global seq

    if len(seq) == n:
        print_seqeunce()
        return

    for i in range(1, n+1):
        if visited[i]:
            continue

        seq.append(i)
        visited[i] = 1

        append_seq()

        seq.pop()
        visited[i] = 0

    return

append_seq()
