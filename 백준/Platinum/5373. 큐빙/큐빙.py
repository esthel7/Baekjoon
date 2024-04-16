import sys
input=sys.stdin.readline

# 0top, 1front, 2bottom, 3back, 4left, 5right

def change(fs,fidx,ss,sidx):
  tmp=[]
  for idx in fidx:
    tmp.append(box[fs][idx])
  for i in range(3):
    box[fs][fidx[i]]=box[ss][sidx[i]]
    box[ss][sidx[i]]=tmp[i]


def reverseclockwise(idx):
  tmp=list(box[idx])
  box[idx]=[tmp[2],tmp[5],tmp[8],tmp[1],tmp[4],tmp[7],tmp[0],tmp[3],tmp[6]]


def clockwise(idx):
  tmp=list(box[idx])
  box[idx]=[tmp[6],tmp[3],tmp[0],tmp[7],tmp[4],tmp[1],tmp[8],tmp[5],tmp[2]]


n=int(input())
for _ in range(n):
  N=int(input())
  now=input().rstrip().split()

  box=[['w','w','w','w','w','w','w','w','w'],['r','r','r','r','r','r','r','r','r'],['y','y','y','y','y','y','y','y','y'],['o','o','o','o','o','o','o','o','o'],['g','g','g','g','g','g','g','g','g'],['b','b','b','b','b','b','b','b','b']]

  for howto in now:
    dir=howto[0]
    clock=howto[1]

    if dir=='U':
      if clock=='-':
        # left, back, right, front 한면씩 이동
        change(4,[0,1,2],3,[2,1,0])
        change(3,[2,1,0],5,[2,1,0])
        change(5,[2,1,0],1,[0,1,2])
        reverseclockwise(0)
      else:
        change(1,[0,1,2],5,[2,1,0])
        change(5,[2,1,0],3,[2,1,0])
        change(3,[2,1,0],4,[0,1,2])
        clockwise(0)
    elif dir=='D':
      if clock=='-':
        # front, right, back, left 한면씩 이동
        change(1,[6,7,8],5,[8,7,6])
        change(5,[8,7,6],3,[8,7,6])
        change(3,[8,7,6],4,[6,7,8])
        clockwise(2)
      else:
        change(4,[6,7,8],3,[8,7,6])
        change(3,[8,7,6],5,[8,7,6])
        change(5,[8,7,6],1,[6,7,8])
        reverseclockwise(2)
    elif dir=='F':
      if clock=='-':
        # left, top, right, bottom 한면씩 이동
        change(4,[8,5,2],0,[6,7,8])
        change(0,[6,7,8],5,[2,5,8])
        change(5,[2,5,8],2,[0,1,2])
        reverseclockwise(1)
      else:
        change(2,[0,1,2],5,[2,5,8])
        change(5,[2,5,8],0,[6,7,8])
        change(0,[6,7,8],4,[8,5,2])
        clockwise(1)
    elif dir=='B':
      if clock=='-':
        # top, left, bottom, right 한면씩 이동
        change(0,[0,1,2],4,[6,3,0])
        change(4,[6,3,0],2,[6,7,8])
        change(2,[6,7,8],5,[0,3,6])
        clockwise(3)
      else:
        change(5,[0,3,6],2,[6,7,8])
        change(2,[6,7,8],4,[6,3,0])
        change(4,[6,3,0],0,[0,1,2])
        reverseclockwise(3)
    elif dir=='L':
      if clock=='-':
        # top, front, bottom, back 한면씩 이동
        change(0,[0,3,6],1,[0,3,6])
        change(1,[0,3,6],2,[2,5,8])
        change(2,[2,5,8],3,[6,3,0])
        reverseclockwise(4)
      else:
        change(3,[6,3,0],2,[2,5,8])
        change(2,[2,5,8],1,[0,3,6])
        change(1,[0,3,6],0,[0,3,6])
        clockwise(4)
    else:
      if clock=='-':
        # top, back, bottom, front 한면씩 이동
        change(0,[8,5,2],3,[2,5,8])
        change(3,[2,5,8],2,[6,3,0])
        change(2,[6,3,0],1,[8,5,2])
        clockwise(5)
      else:
        change(1,[8,5,2],2,[6,3,0])
        change(2,[6,3,0],3,[2,5,8])
        change(3,[2,5,8],0,[8,5,2])
        reverseclockwise(5)

  for i in range(0,9,3):
    for j in range(i,i+3):
      print(box[0][j],end='')
    print()

