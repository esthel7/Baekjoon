def find(N,M,num):
  if len(num)==M:
    for answer in num:
      print(answer, end= ' ')
    print()
    return

  for i in range(N):
    num.append(l[i])
    find(N,M,num)
    num.pop()


N,M=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
find(N,M,[])
