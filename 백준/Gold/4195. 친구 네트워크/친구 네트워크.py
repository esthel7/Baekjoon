import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
  F=int(input())
  info={}
  root=[0 for i in range(F)]

  def change(a,b):
    for key in info.keys():
      if info[key]==a:
        info[key]=b
        root[b]+=1

  for i in range(F):
    a,b=input().rstrip().split()
    if a in info:
      if b in info:
        if info[a]!=info[b]:
          if info[a]<info[b]:
            key=info[a]
            change(info[b],info[a])
          else:
            key=info[b]
            change(info[a],info[b])
        else:
          key=info[a]
      else:
        info[b]=info[a]
        root[info[a]]+=1
        key=info[a]
    else:
      if b in info:
        info[a]=info[b]
        root[info[b]]+=1
        key=info[b]
      else:
        info[a]=i
        info[b]=i
        root[i]+=2
        key=i

    print(root[key])

