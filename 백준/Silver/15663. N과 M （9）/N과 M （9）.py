import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def find(N,M,num,numbers,info):
  if len(num)==M:
    for [answer,flag] in numbers:
      print(answer,end=' ')
    print()
    return

  for i in range(N):
    if i in num:
      continue

    breakFlag=False
    keyFlag=False
    for keys in info.keys():
      if l[i][0]==keys:
        if l[i][1]==info[keys] and l[i][1]<M:
          info[keys]+=1
        else:
          breakFlag=True
        keyFlag=True
        break

    if breakFlag:
      continue
    if not keyFlag:
      info[l[i][0]]=1

    num.append(i)
    numbers.append([l[i][0],l[i][1]])
    find(N,M,num,numbers,info)
    num.pop()
    numbers.pop()
    info[l[i][0]]-=1

N,M=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
l[0]=[l[0],0]
for i in range(1,len(l)):
  if l[i]==l[i-1][0]:
    l[i]=[l[i],l[i-1][1]+1]
  else:
    l[i]=[l[i],0]

find(len(l),M,[],[],{})
