A = input()

# Write your code here!
def run_length_encoding(li):
    encode_string = ''
    prev = None
    cnt = 0
    for c in li:
        if c != prev:
            encode_string += str(cnt)
            encode_string += c
            cnt = 0
        prev = c
        cnt += 1
    encode_string += str(cnt)
    return len(encode_string) - 1

answer = 1e9
for i in range(len(A)):
    li = list(A)[i:] + list(A)[:i]
    answer = min(answer, run_length_encoding(li))

print(answer)