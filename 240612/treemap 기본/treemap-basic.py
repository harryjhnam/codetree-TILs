from sortedcontainers import SortedDict

n = int(input())

sd = SortedDict()
for _ in range(n):
    cmd = input().split()
    c = cmd[0]

    if c == 'add':
        k = int(cmd[1])
        sd[k] = cmd[2]
    elif c == 'remove':
        k = int(cmd[1])
        sd.pop(k)
    elif c == 'find':
        k = int(cmd[1])
        if k in sd:
            print(sd[k])
        else:
            print("None")
    elif c == 'print_list':
        if sd:
            print(' '.join(sd.values()))
        else:
            print("None")