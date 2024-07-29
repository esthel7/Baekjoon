import sys
input=sys.stdin.readline

N=int(input())
l=list(map(int,input().split()))

info={}
for i in range(N):
  prev=0
  if l[i] in info:
    prev=len(info[l[i]])
  appendList=[]
  for key in info.keys():
    if key>=l[i]:
      continue
    if len(info[key])+1>prev:
      prev=len(info[key])+1
      appendList=info[key]+[l[i]]
  if not appendList:
    if l[i] not in info:
      info[l[i]]=[l[i]]
  else:
    info[l[i]]=appendList

answer=0
answers=[]
for keys in info.keys():
  if answer<len(info[keys]):
    answer=len(info[keys])
    answers=info[keys]

print(answer)
for item in answers:
  print(item,end=' ')
print()

# 5
# 1 2 10 4 5
