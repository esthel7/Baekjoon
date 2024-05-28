import sys
input=sys.stdin.readline

while True:
  try:
    x=int(input())*10000000 # 구멍 너비
    n=int(input()) # 레고 개수
    info={}
    for i in range(n):
      a=int(input())
      if a in info:
        info[a]+=1
      else:
        info[a]=1

    L=list(info.keys())
    L.sort()
    continueflag=False
    for key in L:
      left=x-key
      if left in info:
        if left==key and info[left]>=2:
          print('yes',key,left)
          continueflag=True
        elif left!=key:
          print('yes',key,left)
          continueflag=True
        break

    if not continueflag:
      print('danger')
  except:
    break
