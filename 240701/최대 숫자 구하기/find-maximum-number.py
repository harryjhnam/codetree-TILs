from sortedcontainers import SortedSet

n, m = map(int, input().split())

# li = set(range(m, 0, -1))
# deletes = list(map(int, input().split()))

# deleteds = set()
# for i in range(n):
#     deleteds.add(deletes[i])
#     for res in li:
#         if res not in deleteds:
#             print(res)
#             break

li = SortedSet(range(m, 0, -1)) # m*log(m)
deletes = list(map(int, input().split()))
for d in deletes:
    li.remove(d) # log(m)
    print(li[-1])