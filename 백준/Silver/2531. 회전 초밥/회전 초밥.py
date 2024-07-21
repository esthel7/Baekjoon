import sys
input=sys.stdin.readline

# k개 접시 연속해 먹으면 할인가격
# k개 접시 연속해 먹으면 쿠폰 초밥 무료 제공(없다면 만들어 제공)

def update(item):
  if item in info:
    info[item]+=1
  else:
    info[item]=1

N,d,k,c=map(int,input().split())
l=[]
for i in range(N):
  l.append(int(input()))
l=l+l

info={}
for i in range(k):
  update(l[i])

answer=len(info.keys())
if c not in info:
  answer+=1

for i in range(1,N):
  update(l[i+k-1])
  if info[l[i-1]]==1:
    info.pop(l[i-1])
  else:
    info[l[i-1]]-=1
  now=len(info.keys())
  if c not in info:
    now+=1
  answer=max(answer,now)

print(answer)
