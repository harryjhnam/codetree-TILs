n = int(input())
l1 = set(map(int, input().split()))
m = int(input())
l2 = list(map(int, input().split()))

for n in l2:
    if n in l1:
        print(1, end=' ')
    else:
        print(0, end=' ')