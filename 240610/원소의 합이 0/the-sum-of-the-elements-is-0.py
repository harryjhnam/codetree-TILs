from collections import Counter

n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

A_cnt = Counter(A)
B_cnt = Counter(B)
C_cnt = Counter(C)
D_cnt = Counter(D)

AB_cnt = Counter()
for a in A_cnt:
    for b in B_cnt:
        AB_cnt[a+b] += A_cnt[a] * B_cnt[b]

CD_cnt = Counter()
for c in C_cnt:
    for d in D_cnt:
        CD_cnt[c+d] += C_cnt[c] * D_cnt[d]

res = 0
for ab in AB_cnt:
    cd = -ab
    res += AB_cnt[ab] * CD_cnt[cd]

print(res)