def find(N,M,num):
  if len(num)==M:
    for answer in num:
      print(answer,end=' ')
    print()
    return
  
  for i in range(N):
    if l[i] in num:
      continue
    num.append(l[i])
    find(N,M,num)
    num.pop()

N,M=map(int,input().split())
l=[i for i in range(1,N+1)]
find(N,M,[])