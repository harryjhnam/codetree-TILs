from collections import Counter

s = input()
cnt = Counter(s)

res = None
for c in s:
    if cnt[c] == 1:
        res = c
        break

if res == None:
    print("None")
else:
    print(res)