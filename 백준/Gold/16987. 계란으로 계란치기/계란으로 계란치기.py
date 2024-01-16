import sys
input=sys.stdin.readline

# 계란은 상대 무게만큼 깎이고, 내구도가 0이하면 깨짐
# 가장 왼쪽 계란으로 하나 치기
# 손에 든 계란 깨지거나 아무것도 안깨지면 넘어감
# 가장 오른쪽 계란은 들 수 없음

def find(N,l,start,now):
  if start>=N:
    if now>cnt[0]:
      cnt[0]=now
    return

  [p,w]=l[start]

  for i in range(N):
    if i==start:
      continue
    [attackedP, attackedW]=l[i]
    p-=attackedW
    attackedP-=w

    if p<=0:
      l.pop(start)
      if attackedP<=0: # b b
        if start<i:
          l.pop(i-1)
          find(N-2,l,start,now+2)
          l.insert(i-1,[attackedP+w,attackedW])
        else:
          l.pop(i)
          find(N-2,l,start-1,now+2)
          l.insert(i,[attackedP+w,attackedW])
      else: # b l
        if start<i:
          l[i-1][0]=attackedP
          find(N-1,l,start,now+1)
          l[i-1][0]+=w
        else:
          l[i][0]=attackedP
          find(N-1,l,start,now+1)
          l[i][0]+=w
      p+=attackedW
      l.insert(start,[p,w])
    else:
      l[start][0]=p
      if attackedP<=0: # l b
        l.pop(i)
        if start<i:
          find(N-1,l,start+1,now+1)
        else:
          find(N-1,l,start,now+1)
        l.insert(i,[attackedP+w,attackedW])
      else: # l l
        l[i][0]=attackedP
        find(N,l,start+1,now)
        l[i][0]+=w
      p+=attackedW
      l[start][0]=p

  if now>cnt[0]:
    cnt[0]=now


N=int(input())
l=[]
for i in range(N):
  l.append(list(map(int,input().split())))

cnt=[0]
find(N,l,0,0)
print(cnt[0])
