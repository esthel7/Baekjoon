N = int(input())
M = int(input())
S = input()
P = 'IO'*N + 'I'
answer = 0

for i in range(M - len(P)+1):
    if S[i] == 'I':
        if S[i:i+len(P)] == P:
            answer += 1
print(answer)