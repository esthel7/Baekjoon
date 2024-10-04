import sys
input=sys.stdin.readline

N,M=map(int,input().split())
m=list(map(int,input().split()))
c=list(map(int,input().split()))

info={}
answer=sum(c)
for i in range(N):
  if c[i]>=answer:
    continue

  newInfo={}
  for key in info.keys():
    newInfo[key]=info[key]

  for key in info.keys():
    if key+c[i]>=answer:
      continue
    if key+c[i] in info:
      newInfo[key+c[i]]=max(info[key]+m[i],info[key+c[i]])
    else:
      newInfo[key+c[i]]=info[key]+m[i]
    if newInfo[key+c[i]]>=M:
      answer=min(answer,key+c[i])
      newInfo.pop(key+c[i])

  if c[i] in info:
    if c[i] in newInfo:
      newInfo[c[i]]=max(info[c[i]],m[i],newInfo[c[i]])
    else:
      newInfo[c[i]]=max(info[c[i]],m[i])
  else:
    if c[i] in newInfo:
      newInfo[c[i]]=max(m[i],newInfo[c[i]])
    else:
      newInfo[c[i]]=m[i]

  if newInfo[c[i]]>=M:
    answer=min(answer,c[i])
    newInfo.pop(c[i])

  info=newInfo


print(answer)


# 19 20169
# 240 2560 434 6 31 577 500 2715 2916 952 2490 258 1983 1576 3460 933 1660 2804 2584
# 82 77 81 0 36 6 53 78 49 82 82 33 66 8 60 0 98 91 93

# 484
