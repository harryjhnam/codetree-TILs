from sortedcontainers import SortedSet

s = SortedSet()

n = int(input())

for _ in range(n):
    cmd = input()
    if cmd not in ['largest', 'smallest']:
        cmd, x = cmd.split()
        x = int(x)
    if cmd == 'add':
        s.add(x)
    elif cmd == 'remove':
        s.remove(x)
    elif cmd == 'find':
        if x in s:
            print("true")
        else:
            print("false")
    elif cmd == 'lower_bound':
        i = s.bisect_left(x)
        if i == len(s):
            print("None")
        else:
            print(s[i])
    elif cmd == 'upper_bound':
        i = s.bisect_right(x)
        if i == len(s):
            print("None")
        else:
            print(s[i])
    elif cmd == 'largest':
        if s:
            print(s[-1])
        else:
            print("None")
    elif cmd == 'smallest':
        if s:
            print(s[0])
        else:
            print("None")