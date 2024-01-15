def find(L,C,start,num,jnum,mnum):
  if len(num)==L:
    if jnum>=2 and mnum>=1:
      print(''.join(num))
    return

  if start==C:
    return

  for i in range(start,C):
    num.append(l[i])
    if l[i] in mbox:
      find(L,C,i+1,num,jnum,mnum+1)
    else:
      find(L,C,i+1,num,jnum+1,mnum)
    num.pop()

L,C=map(int,input().split())
l=list(input().split())
l.sort()

# 최소 한개의 모음, 두개의 자음
# 사전순

mbox=['a','e','i','o','u']
find(L,C,0,[],0,0)
