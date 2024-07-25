import sys
input=sys.stdin.readline

n=int(input())
l=list(map(int,input().split()))

info={}
info[1]={l[0]:True}
for i in range(1,n):
  for key in reversed(info.keys()):
    breakFlag=False
    for item in info[key].keys():
      if item<l[i]:
        info[key+1]={l[i]:True}
        breakFlag=True
        break
    if breakFlag:
      break
  if not breakFlag:
    info[1][l[i]]=True

answer=list(info.keys())
print(answer[-1])
