n = int(input())
s = set()
for _ in range(n):
    cmd, x = input().split()
    if cmd == 'add':
        s.add(x)
    elif cmd == 'remove':
        s.remove(x)
    elif cmd == 'find':
        if x in s:
            print("true")
        else:
            print("false")