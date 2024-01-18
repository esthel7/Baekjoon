def find(N,M,start,info,num,numbers):
  if len(num)==M:
    for answer in numbers:
      print(answer,end=' ')
    print()
    return

  for i in range(start,N):
    if i in num:
      continue
    if l[i][1]==info[l[i][0]]:
      info[l[i][0]]+=1
      num.append(i)
      numbers.append(l[i][0])
      find(N,M,i+1,info,num,numbers)
      num.pop()
      numbers.pop()
      info[l[i][0]]-=1


N,M=map(int,input().split())
l=list(map(int,input().split()))
l.sort()

l[0]=[l[0],1]
info={l[0][0]:1}

for i in range(1,N):
  if l[i-1][0]==l[i]:
    l[i]=[l[i],l[i-1][1]+1]
  else:
    l[i]=[l[i],1]
    info[l[i][0]]=1

find(N,M,0,info,[],[])
