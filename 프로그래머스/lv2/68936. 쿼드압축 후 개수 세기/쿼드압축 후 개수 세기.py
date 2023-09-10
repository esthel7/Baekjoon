def run(arr,num,z,o):
    if num>len(arr):
        return [z,o]
    
    for i in range(0,len(arr),num):
        for j in range(0,len(arr),num):
            value=arr[i][j]
            if value==-1:
                continue
            
            if arr[i][j+num//2]==value and arr[i+num//2][j]==value and arr[i+num//2][j+num//2]==value:
                if value==0:
                    z-=3
                else:
                    o-=3
            else:
                arr[i][j]=-1  
    return run(arr,num*2,z,o)


def solution(arr):
    z=0
    o=0
    if len(arr)==1:
        if arr[0][0]==0:
            return [1,0]
        return [0,1]
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j]==0:
                z+=1
            else:
                o+=1
    
    answer = run(arr,2,z,o)
    return answer