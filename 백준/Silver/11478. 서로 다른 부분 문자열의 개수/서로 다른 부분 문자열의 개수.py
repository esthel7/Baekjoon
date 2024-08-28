import sys
input=sys.stdin.readline

S=input().rstrip()
info={}
for i in range(len(S)):
  now=S[i]
  info[now]=True
  for j in range(i+1,len(S)):
    now+=S[j]
    info[now]=True

print(len(info.keys()))
