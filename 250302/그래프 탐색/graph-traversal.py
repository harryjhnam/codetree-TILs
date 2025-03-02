n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
graph = [[] for _ in range(n+1)]
for v1, v2 in edges:
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [0 for _ in range(n+1)]
def dfs(v):
    global answer, visited
    for next_v in graph[v]:
        if not visited[next_v]:
            visited[next_v] = 1
            dfs(next_v)

visited[1] = 1
dfs(1)

print(sum(visited) - 1)