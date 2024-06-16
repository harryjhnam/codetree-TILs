N, M = map(int, input().split())
A, B = [], []
for _ in range(N):
    A.append(input())
for _ in range(N):
    B.append(input())

res = 0
for i in range(M-2):
    for j in range(i+1, M-1):
        for k in range(j+1, M):
            a = set([A[r][i]+A[r][j]+A[r][k] for r in range(N)])
            b = set([B[r][i]+B[r][j]+B[r][k] for r in range(N)])
            if not a & b:
                res += 1
                
print(res)