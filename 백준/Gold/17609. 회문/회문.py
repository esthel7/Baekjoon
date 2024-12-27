import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
  l=list(input().rstrip())
  N=len(l)
  q=[[0,N-1,0]]
  flag=False
  while q:
    left,right,cnt=q.pop()
    if l[left]==l[right]:
      left+=1
      right-=1
      if left==right or left>right:
        flag=True
        if cnt==0:
          print(0)
        else:
          print(1)
        break
      q.append([left,right,cnt])
      continue
    elif cnt==0:
      if left+1==right or left==right-1:
        flag=True
        print(1)
        break
      q.append([left+1,right,1])
      q.append([left,right-1,1])
  if not flag:
    print(2)

