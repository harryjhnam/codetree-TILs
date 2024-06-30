from sortedcontainers import SortedSet

T = int(input())

for _ in range(T):
    k = int(input())
    s = SortedSet()
    for _ in range(k):
        cmd, i = input().split()
        i = int(i)
        
        if cmd == 'I':
            s.add(i)
        elif cmd == 'D' and s:
            if i == 1:
                s.remove(s[-1])
            elif i == -1:
                s.remove(s[0])
    if not s:
        print("EMPTY")
    else:
        print(s[-1], s[0])