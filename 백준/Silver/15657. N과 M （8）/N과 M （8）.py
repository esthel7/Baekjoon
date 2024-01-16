def find(N,M,start,num):
  if len(num)==M:
    for answer in num:
      print(answer,end=' ')
    print()
    return

  for i in range(start,N):
    num.append(l[i])
    find(N,M,i,num)
    num.pop()

N,M=map(int,input().split())
l=list(map(int,input().split()))
l.sort()

find(N,M,0,[])
