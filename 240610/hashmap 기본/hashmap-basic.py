n = int(input())
d = dict()
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'add':
        k, v = int(cmd[1]), int(cmd[2])
        d[k] = v
    elif cmd[0] == 'find':
        k = int(cmd[1])
        if k in d:
            print(d[k])
        else:
            print("None")
    elif cmd[0] == 'remove':
        k = int(cmd[1])
        d.pop(k)