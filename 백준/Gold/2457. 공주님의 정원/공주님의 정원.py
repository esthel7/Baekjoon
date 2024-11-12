import sys
input=sys.stdin.readline

# 3.1 ~ 11.30
def find(sm,sd,lm,ld,num,idx): # sm,sd,lm,ld는 한 송이만 있는 경우
  for i in range(idx,N):
    [nsm,nsd,nlm,nld]=l[i]
    if nsm>lm or (nsm==lm and nsd>ld): # 1, idx
      print(0)
      exit()
    if nlm<lm or (nlm==lm and nld<=ld): # idx, 1
      continue

    if nsm<sm or (nsm==sm and nsd<=sd): # idxS, 1, idxE
      if nlm>11:
        print(num)
        exit()
      find(sm,sd,nlm,nld,num,i+1)
      return
    elif nsm<lm or (nsm==lm and nsd<=ld): # 1S, idxS, 1E, idxE
      if nlm>11:
        print(num+1)
        exit()
      find(lm,ld,nlm,nld,num+1,i+1)
      return
    else: # 1E, idx
      print(0)
      exit()



N=int(input())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))
l.sort()

if l[0][0]>3 or (l[0][0]==3 and l[0][1]>1):
  print(0)
  exit()

if l[0][2]>11:
  print(1)
  exit()
find(3,1,l[0][2],l[0][3],1,1)
print(0)

# ~5.31 / 5.15~8.31 -> 5.31~8.31
