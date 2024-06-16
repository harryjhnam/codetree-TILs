N, G = map(int, input().split())
groups = []
for _ in range(G):
    li = list(map(int, input().split()))
    n = li[0]
    groups.append(set(li[1:]))

invited = set()
invited.add(1)
while True:
    updated = False
    for group in groups:
        if len(group - invited) == 1:
            invited = invited | group
            updated = True

    if not updated:
        break

print(len(invited))