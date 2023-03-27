l=list(input())
s=[]
total=[0 for i in range(len(l))]
flag=0
if l[0]==']' or l[0]==')':
    print(0)
    flag=1
elif l[0]=='(' or l[0]=='[':
    for i in range(len(l)):
        if l[i]=='(' or l[i]=='[':
            s.append([i,l[i]])
        elif l[i]==')':
            if len(s)==0:
                print(0)
                flag=1
                break
            if s[len(s)-1][1]!='(':
                print(0)
                flag=1
                break
            if l[i-1]=='(':
                total[i]=2
                del(s[len(s)-1])
            else:
                cnt=0
                for j in range(s[len(s)-1][0]+1,i):
                    cnt=cnt+total[j]
                    total[j]=0
                total[i]=cnt*2
                del(s[len(s)-1])
        elif l[i]==']':
            if len(s)==0:
                print(0)
                flag=1
                break
            if s[len(s)-1][1]!='[':
                print(0)
                flag=1
                break
            if l[i-1]=='[':
                total[i]=3
                del(s[len(s)-1])
            else:
                cnt=0
                for j in range(s[len(s)-1][0]+1,i):
                    cnt=cnt+total[j]
                    total[j]=0
                total[i]=cnt*3
                del(s[len(s)-1])
        else:
            print(0)
            flag=1
            break
else:
    print(0)
    flag=1
if flag==0:
    if len(s)!=0:
        print(0)
    else:
        cnt=0
        for i in range(len(l)):
            cnt=cnt+total[i]
        print(cnt)