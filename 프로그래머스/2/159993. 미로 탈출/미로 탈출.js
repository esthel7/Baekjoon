function solution(maps) {
    function init(){
        for (let i=0;i<n;i++){
            visit.push([])
            for (let j=0;j<m;j++){
                visit[i].push(-1)
            }
        }
    }

    var answer = -1;
    n=maps.length
    for (let i=0;i<n;i++){
        maps[i]=[...maps[i]]
        m=maps[i].length
        for (let j=0;j<m;j++){
            if (maps[i][j]=='S') {
                maps[i][j]='O'
                start=[i,j]
            }
            else if (maps[i][j]=='E') {
                maps[i][j]='O'
                exits=[i,j]
            }
            else if (maps[i][j]=='L') {
                maps[i][j]='O'
                btn=[i,j]
            }
        }
    }
    
    q=[[start[0],start[1],0]]
    visit=[]
    init()
    xbox=[-1,1,0,0]
    ybox=[0,0,-1,1]
    btnflag=false
    btncnt=0
    
    while (q.length!=0){
        [x,y,cnt]=q.shift()
        if (x==btn[0]&&y==btn[1]){
            btnflag=true
            btncnt=cnt
            break
        }
        if (maps[x][y]=='X') continue
        if (visit[x][y]==-1 || visit[x][y]>cnt){
            visit[x][y]=cnt
            for(let i=0;i<4;i++){
                newX=x+xbox[i]
                newY=y+ybox[i]
                if (0<=newX && newX<n && 0<=newY && newY<m){
                    q.push([newX,newY,cnt+1])
                }
            }
        }
    }
    
    if (!btnflag) return -1;
    
    q=[[btn[0],btn[1],btncnt]]
    visit=[]
    init()
    
    while (q.length!=0){
        [x,y,cnt]=q.shift()
        if (x==exits[0]&&y==exits[1]){
            answer=cnt
            break
        }
        if (maps[x][y]=='X') continue
        if (visit[x][y]==-1 || visit[x][y]>cnt){
            visit[x][y]=cnt
            for(let i=0;i<4;i++){
                newX=x+xbox[i]
                newY=y+ybox[i]
                if (0<=newX && newX<n && 0<=newY && newY<m){
                    q.push([newX,newY,cnt+1])
                }
            }
        }
    }
    
    return answer;
}