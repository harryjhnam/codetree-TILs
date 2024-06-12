N, K = map(int, input().split())
swaps = []
for _ in range(K):
    swaps.append(tuple(map(int, input().split())))

locs = list(range(N+1))
visited = [set([i]) for i in range(N+1)]

for a_i, b_i in swaps*3:
    A, B = locs[a_i], locs[b_i]
    visited[A].add(b_i)
    visited[B].add(a_i)
    locs[a_i], locs[b_i] = B, A

for s in visited[1:]:
    print(len(s))