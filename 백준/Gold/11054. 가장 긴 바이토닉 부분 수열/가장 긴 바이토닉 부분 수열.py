import sys
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split()))

big=[1 for i in range(N)]
save=[[l[0]]]
for i in range(1,N):
  insertFlag=False
  Save=len(save)
  for j in range(Save-1,-1,-1):
    for k in range(len(save[j])):
      if save[j][k]<l[i]:
        if Save>j+1:
          save[j+1].append(l[i])
          big[i]=j+2
        else:
          save.append([l[i]])
          big[i]=Save+1
        insertFlag=True
        break
    if insertFlag:
      break
  if not insertFlag:
    save[0].append(l[i])

small=[1 for i in range(N)]
save=[[l[N-1]]]
for i in range(N-2,-1,-1):
  insertFlag=False
  Save=len(save)
  for j in range(Save-1,-1,-1):
    for k in range(len(save[j])):
      if save[j][k]<l[i]:
        if Save>j+1:
          save[j+1].append(l[i])
          small[i]=j+2
        else:
          save.append([l[i]])
          small[i]=Save+1
        insertFlag=True
        break
    if insertFlag:
      break
  if not insertFlag:
    save[0].append(l[i])

final=[0 for i in range(N)]
for i in range(N):
  final[i]=big[i]+small[i]-1

print(max(final))
