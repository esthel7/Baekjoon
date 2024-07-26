import sys
input=sys.stdin.readline

S=input().rstrip()
final=len(S)
N=int(input())

words=[]
wordsLen=[]
for i in range(N):
  words.append(input().rstrip())
  wordsLen.append(len(words[i]))

dp=[False for i in range(final)]
dp[0]=True

for i in range(final):
  if dp[i]:
    for j in range(N):
      if S[i]==words[j][0]:
        if final-i>=wordsLen[j] and S[i:i+wordsLen[j]]==words[j]:
          if i+wordsLen[j]==final:
            print(1)
            exit(0)
          dp[i+wordsLen[j]]=True

print(0)
