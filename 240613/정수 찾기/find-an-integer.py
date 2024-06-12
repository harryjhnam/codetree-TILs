n = int(input())
l1 = set(input().split())
m = int(input())
l2 = list(input().split())

for n in l2:
    if n in l1:
        print(1)
    else:
        print(0)