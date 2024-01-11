def find(A,B,C):
  if B==1:
    return A%C
  elif B%2==0:
    return (find(A,B//2,C)**2)%C
  else:
    return ((find(A,B//2,C)**2)*A)%C

A,B,C=map(int,input().split())
print(find(A,B,C))
