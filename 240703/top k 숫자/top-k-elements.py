from sortedcontainers import SortedSet

n, k = map(int, input().split())
s = SortedSet(map(int, input().split()))
print(" ".join(list(map(str, s[-k:][::-1]))))