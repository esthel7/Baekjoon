import sys
input=sys.stdin.readline

def find():
  last=len(l)
  idx=0
  flag0=False
  flag1=False
  while idx<last:
    if l[idx]=='0':
      if flag0:
        idx+=1
        continue
      else:
        if flag1:
          if idx-2>=0 and l[idx-2]=='1' and idx+1<last and l[idx+1]=='0': # 1 이어져오다가 0으로 바뀜
            flag0=True
            flag1=False
            idx+=2
            continue
          elif idx+1<last and l[idx+1]=='1': # 01
            idx+=2
            flag1=False
            continue
          else:
            print('NO')
            return
        else:
          if idx+1<last and l[idx+1]=='1':
            idx+=2
            continue
          print('NO')
          return
    else: # 1
      if flag0: # 0 이어져오다가 1로 바뀜
        flag0=False
        flag1=True
        idx+=1
        continue
      else:
        if flag1:
          idx+=1
          continue
        else:
          if idx+2<last and l[idx+1]=='0' and l[idx+2]=='0':
            flag0=True
            idx+=3
            continue
          else:
            print('NO')
            return


  if flag0:
    print('NO')
    return
  print('YES')


T=int(input())
for i in range(T):
  l=list(input().rstrip())
  find()

# 100xxx1xxx | 01
