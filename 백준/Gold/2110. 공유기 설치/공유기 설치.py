import sys
input=sys.stdin.readline

N,C=map(int,input().split())
l=[]
for i in range(N):
  l.append(int(input()))

l.sort()

if C==2:
  print(l[-1]-l[0])
  exit(0)

start=1
end=l[-1]-l[0]
while start<end:
  mid=(start+end)//2
  count=1
  last=0
  for i in range(N):
    if l[i]-l[last]>=mid:
      last=i
      count+=1
  if count>=C:
    answer=mid
    start=mid+1
  else:
    end=mid

print(answer)
