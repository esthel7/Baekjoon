import sys
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split()))

info={}
for i in range(N):
  if l[i] in info:
    info[l[i]]+=1
  else:
    info[l[i]]=1

left={}
answer=[-1 for i in range(N)]
for i in range(N):
  Left=list(left.keys())
  for key in Left:
    if key<info[l[i]]:
      for idx in left[key].keys():
        answer[idx]=l[i]
      left.pop(key)
  if info[l[i]] in left:
    left[info[l[i]]][i]=True
  else:
    left[info[l[i]]]={i:True}

print(*answer)
